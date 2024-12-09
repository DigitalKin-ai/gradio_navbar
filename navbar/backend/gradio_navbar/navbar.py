from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, Dict

from gradio.components.base import Component
from gradio.events import Events

if TYPE_CHECKING:
    from gradio.components import Timer


class NavBar(Component):
    """
    Creates a very simple textbox for user to enter string input or display string output.
    """

    EVENTS = [
        # Events.change,
        # Events.input,
        # Events.submit,
    ]

    def __init__(
        self,
        value: Dict[str, Any] | Callable | None = None,
        *,
        every: Timer | float | None = None,
        inputs: Component | Sequence[Component] | set[Component] | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | None = None,
    ):
        """
        Parameters:
            value (Dict[str, Any] | Callable | None): A dictionary containing the parameters for the NavBar.
            every: Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.
            inputs: Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            key: if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.
        """
        # self.placeholder = placeholder
        # self.rtl = rtl
        super().__init__(
            every=every,
            inputs=inputs,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            render=render,
            key=key,
        )

    def preprocess(self, payload: Dict[str, Any] | None) -> Dict[str, Any] | None:
        """
        Parameters:
            payload: the text entered in the textarea.
        Returns:
            Passes text value as a {str} into the function.
        """
        return payload

    def postprocess(self, value: Dict[str, Any] | None) -> Dict[str, Any] | None:
        """
        Parameters:
            value: Expects a {str} returned from function and sets textarea value to it.
        Returns:
            The value to display in the textarea.
        """
        return value

    def update(
        self,
        value: Dict[str, Any] | None = None,
        visible: bool | None = None,
    ) -> Dict[str, Any]:
        """
        Updates the component's properties.

        Args:
            value (Dict[str, Any] | None): The new value for the component.
            visible (bool | None): The visibility of the component.

        Returns:
            Dict[str, Any]: A dictionary with the updated properties.
        """
        return {
            "value": value,
            "visible": visible,
            "__type__": "update",
        }

    def api_info(self) -> Dict[str, Any]:
        """
        Returns the API information for this component.
        """
        return {
            "type": "object",
            "properties": {
                "company_logo_url": {
                    "type": "string",
                    "description": "The URL of the company logo image.",
                },
                "company_name": {
                    "type": "string",
                    "description": "The name of the company.",
                },
                "logout_link": {
                    "type": "string",
                    "description": "The URL for the logout route.",
                },
                "username": {
                    "type": "string",
                    "description": "The username to display.",
                },
                "profile_photo_url": {
                    "type": "string",
                    "description": "The URL of the user's profile photo.",
                },
            },
            "required": [
                "company_logo_url",
                "company_name",
                "logout_link",
                "username",
                "profile_photo_url",
            ],
        }

    def example_payload(self) -> Dict[str, Any]:
        """
        Provides an example value for this component.

        Returns:
            Dict[str, Any]: An example value dictionary.
        """
        return {
            "company_logo_url": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d52",
            "company_name": "Example Corp",
            "logout_link": "/logout",
            "username": "Jane Doe",
            "profile_photo_url": "https://avatar.iran.liara.run/public",
        }

    def example_value(self) -> Dict[str, Any]:
        """
        Provides an example value for this component.

        Returns:
            Dict[str, Any]: An example value dictionary.
        """
        return {
            "company_logo_url": "https://avatar.iran.liara.run/username?username=Example+Corp",
            "company_name": "Example Corp",
            "logout_link": "/logout",
            "username": "Jane Doe",
            "profile_photo_url": "https://avatar.iran.liara.run/public/boy",
        }

    def get_config(self) -> Dict[str, Any]:
        """
        Returns the configuration for this component.
        """
        config = super().get_config()
        config.update({"value": self.value, "visible": self.visible})
        return config
