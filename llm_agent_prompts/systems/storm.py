"""Auto-generated SDK for STORM (2402.14207)."""

from typing import Dict, Any

class STORM:
    """Prompts extracted from: https://github.com/stanford-oval/storm"""

    @staticmethod
    def get_genrelatedtopicsprompt_prompt() -> str:
        """topic\nReturns:\n    related_topics URLs list"""
        return """I'm writing Wikipedia page for topic mentioned below Please identify recommend Wikipedia pages on closely related subjects insights interesting aspects commonly associated typical content structure included in Wikipedia pages similar topics List urls separate lines"""

    @staticmethod
    def get_genperspectivesprompt_prompt() -> str:
        """topic + examples wiki page outlines related topics for inspiration tocs concatenated\nReturns:\n    perspectives P = {p1..pN} + p0 basic fact writer focusing broadly covering basic facts"""
        return """You need to select group Wikipedia editors who will work together create comprehensive article on topic Each represents different perspective role affiliation related to topic You can use other Wikipedia pages related topics inspiration For each editor add description what they will focus on Format 1. short summary editor1: description..."""

    @staticmethod
    def get_genqnprompt_prompt() -> str:
        """topic + persona perspective p + conv history dlg_history\nReturns:\n    question q"""
        return """You are experienced Wikipedia writer want edit specific page Besides identity as Wikipedia writer you have specific focus when researching topic Now you are chatting with expert to get information Ask good questions to get more useful information When no more question say Thank you so much for your help! to end conversation Please only ask one question at a time don't ask what you have asked before Your questions related topic you want write"""

    @staticmethod
    def get_genqueriesprompt_prompt() -> str:
        """topic + question q\nReturns:\n    queries - query1 - query2 ..."""
        return """You want answer question using Google search What do you type search box? Write queries format - query1 - query2..."""

    @staticmethod
    def get_genanswerprompt_prompt() -> str:
        """topic + conv Question + gathered information info sources\nReturns:\n    answer a informative every sentence supported"""
        return """You are expert who can use information effectively chatting with Wikipedia writer who wants write Wikipedia page on topic you know You have gathered related information will now use information to form response Make response as informative as possible make sure every sentence is supported by gathered information"""

    @staticmethod
    def get_directgenoutlineprompt_prompt() -> str:
        """topic t\nReturns:\n    draft outline OD general framework # ## ###"""
        return """Write outline for Wikipedia page Format Use # Title to indicate section title ## Title subsection ### subsubsection etc Do not include other information Leverage internal knowledge LLMs"""

    @staticmethod
    def get_refineoutlineprompt_prompt() -> str:
        """topic t + OD + convos {C0..CN} N+1 conversations M rounds each\nReturns:\n    improved outline O comprehensive # ## ###"""
        return """Improve outline for Wikipedia page You already have draft outline covering general info Now you want improve based on information learned from information-seeking conversation to make more comprehensive Format same # ## ###"""

