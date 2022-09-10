"""
Components/Pickers


.. MDThemePicker:
MDThemePicker
-------------

.. code-block:: python

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

.. image:: https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/MDThemePicker.gif
    :align: center
"""

from kivy import Logger
from kivy.animation import Animation
from kivy.event import EventDispatcher
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import (
    BooleanProperty,
    ColorProperty,
    ListProperty,
    NumericProperty,
    ObjectProperty,
    OptionProperty,
    StringProperty,
)
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import ButtonBehavior, FocusBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.utils import get_color_from_hex
from kivy.vector import Vector

from kivymd.color_definitions import colors, palette
# from kivymd.theming import ThemableBehavior
# from kivymd.toast import toast
from kivymd.uix.behaviors import (
    FakeRectangularElevationBehavior,
    SpecificBackgroundColorBehavior,
)
# from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
# from kivymd.uix.circularlayout import MDCircularLayout
from kivymd.uix.dialog import BaseDialog
# from kivymd.uix.label import MDLabel
# from kivymd.uix.relativelayout import MDRelativeLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.tooltip import MDTooltip


Builder.load_string(
    """
<Tab@MDFloatLayout+MDTabsBase>
    md_bg_color: app.theme_cls.bg_normal


<ColorSelector>
    canvas:
        Color:
            rgba: root.rgb_hex(root.color_name)
        Ellipse:
            size: self.size
            pos: self.pos


<AccentColorSelector@ColorSelector>
    on_release: app.theme_cls.accent_palette = root.color_name


<PrimaryColorSelector@ColorSelector>
    on_release: app.theme_cls.primary_palette = root.color_name


<MDThemePicker>
    size_hint: None, None
    size: "284dp", "400dp"

    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Change theme"

        MDTabs:
            on_tab_switch: root.on_tab_switch(*args)

            Tab:
                id: theme_tab
                text: "Theme"

                MDGridLayout:
                    id: primary_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

            Tab:
                text: "Accent"

                MDGridLayout:
                    id: accent_box
                    adaptive_size: True
                    spacing: "8dp"
                    padding: "12dp"
                    pos_hint: {"center_x": .5, "top": 1}
                    cols: 5
                    rows: 4

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()

            Tab:
                text: "Style"

                MDGridLayout:
                    adaptive_size: True
                    spacing: "8dp"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    cols: 2
                    rows: 1

                    MDIconButton:
                        canvas:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 1.
                                circle: (self.center_x, self.center_y, sp(62))

                        user_font_size: "100sp"
                        on_release: app.theme_cls.theme_style = "Light"

                    MDIconButton:
                        canvas:
                            Color:
                                rgba: 0, 0, 0, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos

                        on_release: app.theme_cls.theme_style = "Dark"
                        user_font_size: "100sp"

                MDFlatButton:
                    text: "CLOSE"
                    pos: root.width - self.width - 10, 10
                    on_release: root.dismiss()
"""
)


class ColorSelector(MDIconButton):
    color_name = OptionProperty("Indigo", options=palette)

    def rgb_hex(self, col):
        return get_color_from_hex(colors[col][self.theme_cls.accent_hue])


class MDThemePicker(
    BaseDialog,
    SpecificBackgroundColorBehavior,
    FakeRectangularElevationBehavior,
):
    print("ThPi")

    def on_open(self):
        self.on_tab_switch(None, self.ids.theme_tab, None, None)

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        if instance_tab.text == "Theme":
            if not self.ids.primary_box.children:
                for name_palette in palette:
                    self.ids.primary_box.add_widget(
                        Factory.PrimaryColorSelector(color_name=name_palette)
                    )
        if instance_tab.text == "Accent":
            if not self.ids.accent_box.children:
                for name_palette in palette:
                    self.ids.accent_box.add_widget(
                        Factory.AccentColorSelector(color_name=name_palette)
                    )
