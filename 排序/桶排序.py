mOtherItems();
            }

            if (input.activeFocus) {
                var pos = input.positionAt(mouse.x, mouse.y)
                input.moveHandles(pos, pos)
            }
        }

        onPressAndHold: {
            var pos = input.positionAt(mouseArea.mouseX, mouseArea.mouseY);
            input.select(pos, pos);
            var hasSelection = selectionStart != selectionEnd;
            if (!control.menu || (input.length > 0 && (!input.activeFocus || hasSelection))) {
                selectWord();
            } else {
                // We don't select anything at this point, the
                // menu will instead offer to select a word.
                __showMenuFromTouchAndHold = true;
                menuTimer.start();
                clearFocusFromOtherItems();
            }
        }

        onReleased: __showMenuFromTouchAndHold = false
        onCanceled: __showMenuFromTouchAndHold = false
    }

    Connections {
        target: cursorHandle ? cursorHandle : null
        ignoreUnknownSignals: true
        onPressedChanged: menuTimer.start()
    }

    Connections {
        target: selectionHandle ? selectionHandle : null
        ignoreUnknownSignals: true