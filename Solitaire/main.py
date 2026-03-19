#!uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "flet[all]>=0.27.3",
# ]
# ///

import flet as ft

# Use of GestureDetector with on_pan_update event for dragging card
# Absolute positioning of controls within stack

def main(page: ft.Page):
    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    class Solitaire:
       def __init__(self):
            self.start_top = 0
            self.start_left = 0

    solitaire = Solitaire()
    
    def start_drag(e: ft.DragStartEvent):
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
        e.control.update()
    

    def bounce_back(game, card):
        card.top = game.start_top
        card.left = game.start_left
        page.update()
   
    def drop(e: ft.DragEndEvent):
        if (
            abs(e.control.top - slot.top) < 20
            and abs(e.control.left - slot.left) < 20
        ):
            place(e.control, slot)
        else:
            bounce_back(solitaire, e.control)
        e.control.update()

    def place(card, slot):
        card.top = slot.top
        card.left = slot.left
        page.update()

    card = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
    )

    slot = ft.Container(
        width=70,
        height=100,
        left=200,
        top=0,
        border=ft.border.all(1)
    )
   
   
    page.add(ft.Stack(controls=[slot, card], width=1000, height=500))

ft.run(main)