# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50
class Goal_Mode(Choice):
    """What's your Game Mode/Goal?"""
    display_name = "Game Mode"
    option_Normal = 0
    option_Plundering = 1
    option_VictoryLap = 2
class ProgressiveArea(Choice):
    """How many progressive areas do you want in the pool? (Scarce = 5, Normal = 7, Abundant = 9)"""
    display_name = "Game Mode"
    option_scarce = 0
    option_normal = 1
    option_abundant = 2
class MesaAlpine(Choice):
    """Would you like Mesa checks or Alpine checks or both (If you're unsure what the map has, choose both and check off what it isn't when you find out)"""
    display_name = "Mesa or Alpine"
    option_mesa = 0
    option_alpine = 1
    option_both = 2
class FriendBadges(Toggle):
        """Are you doing PEAK multiplayer and are interested in adding badges that require others?"""
        display_name = "Friend Badges"
class RNGBadges(Toggle):
        """Would you like to add badges that take a good chunk of luck and time to do?"""
        display_name = "RNG Badges"
class CustomBadges(Toggle):
        """Would you like to turn on custom badges that were made for this manual?"""
        display_name = "Custom Badges"
class DeathBadges(Toggle):
        """Would you like to add seperate custom badges based around various ways to pass out in the game?"""
        display_name = "Death Badges"
class LuggageType(Choice):
        """Pick between what luggage checks you want, biome specific luggage (10 per biome except 2 in kiln) or general luggage that you can set the number of"""
        display_name = "Luggage Type"
        option_Biome = 0
        option_General = 1
class GeneralLuggageAmount(Range):
    """How many luggage checks total do you want? (The amount of locations available are based on progressive area item amounts)"""
    display_name = "General Luggage Amount"
    range_start = 5
    range_end = 100
    default = 42
class VictoryLaps(Range):
    """If you picked Victory Lap mode as your game mode, how many victory laps do you want (after the first Peak Badge win), up to 9 laps (10 total Peak Badges)"""
    display_name = "Victory Lap Amount"
    range_start = 1
    range_end = 9
    default = 1
class AscentTraps(Toggle):
        """Would you like to add Ascent Traps into the pool (Whenever you start your next run, you have to up the difficulty)"""
        display_name = "Ascent Traps"
# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["game_mode"] = Goal_Mode
    options["progressive_area"] = ProgressiveArea
    options["mesa_alpine"] = MesaAlpine
    options["friend_badges"] = FriendBadges
    options["rng_badges"] = RNGBadges
    options["custom_badges"] = CustomBadges
    options["death_badges"] = DeathBadges
    options["luggage_type"] = LuggageType
    options["general_luggage_amount"] = GeneralLuggageAmount
    options["victory_laps"] = VictoryLaps   
    options["ascent_traps"] = AscentTraps
    return options
# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
