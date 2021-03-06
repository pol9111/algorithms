    enabled: styleData.enabled
        selected: styleData.selected
        on: styleData.checkable && styleData.checked

        hints: { "showUnderlined": styleData.underlineMnemonic }

        properties: {
            "checkable": styleData.checkable,
            "exclusive": styleData.exclusive,
            "shortcut": styleData.shortcut,
            "type": styleData.type,
            "scrollerDirection": styleData.scrollerDirection,
            "icon": !!__menuItem && __menuItem.__icon
        }

        Accessible.role: Accessible.MenuItem
        Accessible.name: StyleHelpers.removeMnemonics(text)
    }

    property Component scrollIndicator: menuItemPanel

    property Component __scrollerStyle: null
}
                                                                             