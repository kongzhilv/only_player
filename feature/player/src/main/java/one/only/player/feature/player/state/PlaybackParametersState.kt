package one.only.player.feature.player.state

import android.content.Context
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableFloatStateOf
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import androidx.media3.common.Player
import androidx.media3.common.listen
import androidx.media3.common.util.UnstableApi
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.session.MediaController
import kotlin.math.abs
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.launch
import one.only.player.feature.player.service.isSkipSilenceEnabled
import one.only.player.feature.player.service.setPersistentPlaybackSpeed
import one.only.player.feature.player.service.setSkipSilenceEnabled

@UnstableApi
@Composable
fun rememberPlaybackParametersState(player: Player): PlaybackParametersState {
    val scope = rememberCoroutineScope()
    val context = LocalContext.current.applicationContext
    val playbackParametersState = remember(player) {
        PlaybackParametersState(player, scope, context)
    }
    LaunchedEffect(player) { playbackParametersState.observe() }
    return playbackParametersState
}

@UnstableApi
class PlaybackParametersState(
    private val player: Player,
    private val scope: CoroutineScope,
    context: Context,
) {
    private val playbackSpeedPreferences = context.getSharedPreferences(
        PLAYBACK_SPEED_PREFERENCES_NAME,
        Context.MODE_PRIVATE,
    )

    var speed: Float by mutableFloatStateOf(1f)
        private set

    var isSkipSilenceEnabled: Boolean by mutableStateOf(false)
        private set

    fun setPlaybackSpeed(speed: Float) {
        savePlaybackSpeed(speed)
        applyPlaybackSpeed(speed)
    }

    fun setIsSkipSilenceEnabled(isEnabled: Boolean) {
        scope.launch {
            when (player) {
                is MediaController -> player.setSkipSilenceEnabled(isEnabled)
                is ExoPlayer -> player.skipSilenceEnabled = isEnabled
                else -> return@launch
            }
            updateSkipSilenceEnabled()
        }
    }

    suspend fun observe() {
        restoreSavedPlaybackSpeed()
        updateSpeed()
        updateSkipSilenceEnabled()

        player.listen { events ->
            val shouldRestoreSavedSpeed =
                events.contains(Player.EVENT_MEDIA_ITEM_TRANSITION) ||
                    events.contains(Player.EVENT_PLAYBACK_STATE_CHANGED) ||
                    events.contains(Player.EVENT_PLAY_WHEN_READY_CHANGED)

            if (shouldRestoreSavedSpeed) {
                restoreSavedPlaybackSpeed()
            }

            if (events.contains(Player.EVENT_PLAYBACK_PARAMETERS_CHANGED)) {
                updateSpeed()
            }
        }
    }

    private fun savePlaybackSpeed(speed: Float) {
        val key = currentPlaybackSpeedPreferenceKey() ?: return
        playbackSpeedPreferences.edit().putFloat(key, speed).apply()
    }

    private fun restoreSavedPlaybackSpeed() {
        val key = currentPlaybackSpeedPreferenceKey() ?: return
        if (!playbackSpeedPreferences.contains(key)) return

        val savedSpeed = playbackSpeedPreferences.getFloat(key, 1f)
        if (abs(player.playbackParameters.speed - savedSpeed) <= SPEED_EPSILON) return

        applyPlaybackSpeed(savedSpeed)
    }

    private fun currentPlaybackSpeedPreferenceKey(): String? {
        val mediaId = player.currentMediaItem
            ?.mediaId
            ?.takeIf(String::isNotBlank)
            ?: return null
        return "$PLAYBACK_SPEED_KEY_PREFIX$mediaId"
    }

    private fun applyPlaybackSpeed(speed: Float) {
        when (player) {
            is MediaController -> player.setPersistentPlaybackSpeed(speed)
            else -> player.setPlaybackSpeed(speed)
        }
    }

    private fun updateSpeed() {
        speed = player.playbackParameters.speed
    }

    private fun updateSkipSilenceEnabled() {
        scope.launch {
            isSkipSilenceEnabled = when (player) {
                is MediaController -> player.isSkipSilenceEnabled()
                is ExoPlayer -> player.skipSilenceEnabled
                else -> return@launch
            }
        }
    }

    private companion object {
        private const val PLAYBACK_SPEED_PREFERENCES_NAME = "manual_playback_speed"
        private const val PLAYBACK_SPEED_KEY_PREFIX = "media:"
        private const val SPEED_EPSILON = 0.001f
    }
}
