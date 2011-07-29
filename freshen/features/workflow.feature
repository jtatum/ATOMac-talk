Using step definitions from: 'steps/workflow'

Feature: Creating workflows
    In order to automate applications
    As a Macintosh user
    I want to create a workflow in Automator

    Scenario: Basic workflow
        Given an empty workflow
        And an Ask for Text action
        And a Speak Text action
        When I click Run
        And I enter "I'm sorry Dave, I'm afraid I can't do that" in the dialog
        And I click OK in the dialog
        Then the workflow runs successfully within 6 seconds

    Scenario: Short workflow
        Given an empty workflow
        And an Ask for Text action
        When I click Run
        And I enter "A short string of text" in the dialog
        And I click OK in the dialog
        Then the workflow runs successfully within 2 seconds
