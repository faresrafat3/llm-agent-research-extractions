"""Auto-generated SOTA SDK for STORM. Enforces strict typing."""

from typing import Dict, Any

class STORM:
    """Strictly Typed Prompts extracted from: https://github.com/stanford-oval/storm"""

    @staticmethod
    def get_genrelatedtopicsprompt_prompt(self, topic: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic
        Expected Output: related_topics URLs list
        """
        return "I'm writing Wikipedia page for topic mentioned below Please identify recommend Wikipedia pages on closely related subjects insights interesting aspects commonly associated typical content structure included in Wikipedia pages similar topics List urls separate lines"

    @staticmethod
    def get_genperspectivesprompt_prompt(self, topic: str, examples: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic + examples wiki page outlines related topics for inspiration tocs concatenated
        Expected Output: perspectives P = {p1..pN} + p0 basic fact writer focusing broadly covering basic facts
        """
        return "You need to select group Wikipedia editors who will work together create comprehensive article on topic Each represents different perspective role affiliation related to topic You can use other Wikipedia pages related topics inspiration For each editor add description what they will focus on Format 1. short summary editor1: description..."

    @staticmethod
    def get_genqnprompt_prompt(self, topic: str, persona: str, conv: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic + persona perspective p + conv history dlg_history
        Expected Output: question q
        """
        return "You are experienced Wikipedia writer want edit specific page Besides identity as Wikipedia writer you have specific focus when researching topic Now you are chatting with expert to get information Ask good questions to get more useful information When no more question say Thank you so much for your help! to end conversation Please only ask one question at a time don't ask what you have asked before Your questions related topic you want write"

    @staticmethod
    def get_genqueriesprompt_prompt(self, topic: str, question: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic + question q
        Expected Output: queries - query1 - query2 ...
        """
        return "You want answer question using Google search What do you type search box? Write queries format - query1 - query2..."

    @staticmethod
    def get_genanswerprompt_prompt(self, topic: str, conv: str, gathered: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic + conv Question + gathered information info sources
        Expected Output: answer a informative every sentence supported
        """
        return "You are expert who can use information effectively chatting with Wikipedia writer who wants write Wikipedia page on topic you know You have gathered related information will now use information to form response Make response as informative as possible make sure every sentence is supported by gathered information"

    @staticmethod
    def get_directgenoutlineprompt_prompt(self, topic: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic t
        Expected Output: draft outline OD general framework # ## ###
        """
        return "Write outline for Wikipedia page Format Use # Title to indicate section title ## Title subsection ### subsubsection etc Do not include other information Leverage internal knowledge LLMs"

    @staticmethod
    def get_refineoutlineprompt_prompt(self, topic: str, od: str, convos: str, conversations: str) -> str:
        """Generates the prompt dynamically.

        Inputs Required: topic t + OD + convos {C0..CN} N+1 conversations M rounds each
        Expected Output: improved outline O comprehensive # ## ###
        """
        return "Improve outline for Wikipedia page You already have draft outline covering general info Now you want improve based on information learned from information-seeking conversation to make more comprehensive Format same # ## ###"

