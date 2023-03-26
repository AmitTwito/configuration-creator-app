from app.enums.configuration_section_enum import ConfigurationSections
from app.enums.mode_enum import Modes
from app.models.configuration_sections.configuration_section import ConfigurationSection


class ModeSection(ConfigurationSection):
    def __init__(self, configuration_section_type: ConfigurationSections, template_file: str):
        super().__init__(configuration_section_type, template_file)
        self._mode = Modes.DEBUG
        self._form_keys = [{"key": "mode-options", "is_collection": False}]


    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        raise AttributeError('Setting the mode attr is forbidden')

    def validate_from_yaml(self, value):
        modes = {mode.name: mode for mode in Modes}
        if value not in modes.keys():
            return {"error": f"Wrong mode value. Please choose a valid from:{list(modes.keys())}"}

        return Modes.get_by_name(value)

    def update_from_yaml(self, value):
        self._mode = Modes.get_by_name(value)

    def validate(self, value):
        modes_enum_values = [e.value for e in Modes]
        value = int(value)
        if value not in modes_enum_values:
            return {"error": f"Error at reading the mode value from the config file. "
                             f"Wrong integer value for Mode as it needs to be within {value}"}
        return Modes(value)

    def update(self, value: Modes):
        self._mode = value

    def as_dict(self) -> dict:
        return {'mode': self._mode.name}
