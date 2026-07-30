package one.only.player.core.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.widthIn
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalConfiguration
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import top.yukonga.miuix.kmp.basic.Text
import top.yukonga.miuix.kmp.window.WindowDialog

@Composable
fun NextDialog(
    onDismissRequest: () -> Unit,
    title: @Composable () -> Unit,
    content: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    confirmButton: @Composable () -> Unit,
    dismissButton: @Composable (() -> Unit)? = null,
) {
    val configuration = LocalConfiguration.current
    val maxDialogHeight = configuration.screenHeightDp.dp - NextDialogDefaults.dialogMargin * 2

    WindowDialog(
        show = true,
        modifier = modifier
            .widthIn(max = configuration.screenWidthDp.dp - NextDialogDefaults.dialogMargin * 2)
            .heightIn(max = maxDialogHeight),
        onDismissRequest = onDismissRequest,
    ) {
        Column(
            modifier = Modifier.heightIn(max = maxDialogHeight),
        ) {
            Column {
                title()
            }
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .weight(1f, fill = false),
            ) {
                content()
            }
            NextDialogButtonRow(
                confirmButton = confirmButton,
                dismissButton = dismissButton,
            )
        }
    }
}

@Composable
fun NextDialog(
    onDismissRequest: () -> Unit,
    title: String,
    content: @Composable () -> Unit,
    modifier: Modifier = Modifier,
    confirmButton: @Composable () -> Unit,
    dismissButton: @Composable (() -> Unit)? = null,
) {
    NextDialog(
        onDismissRequest = onDismissRequest,
        title = { Text(text = title) },
        content = content,
        modifier = modifier,
        confirmButton = confirmButton,
        dismissButton = dismissButton,
    )
}

@Composable
fun NextDialogWithDoneAndCancelButtons(
    title: String,
    onDoneClick: () -> Unit,
    onDismissClick: () -> Unit,
    content: @Composable () -> Unit,
) {
    NextDialog(
        title = title,
        confirmButton = { DoneButton(onClick = onDoneClick) },
        dismissButton = { CancelButton(onClick = onDismissClick) },
        onDismissRequest = onDismissClick,
        content = content,
    )
}

@Composable
private fun NextDialogButtonRow(
    confirmButton: @Composable () -> Unit,
    dismissButton: @Composable (() -> Unit)?,
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(top = 12.dp),
        horizontalArrangement = Arrangement.spacedBy(12.dp, Alignment.End),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        dismissButton?.invoke()
        confirmButton()
    }
}

object NextDialogDefaults {
    val dialogMargin: Dp = 16.dp
}
