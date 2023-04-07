# BLPackageManager

This project is intended to ease the onboarding process for new BL participants.

## About
- This application shall allow for a customizable onboarding experience of new participants at BL.
- It is intended for usage by the BL management during the onboarding process of new participants.
- It solves the problem that currently participants and coaches do not get a great overview of the coaching plan.
- The application will be based on high-level packages that can be customized with additional coaching modules.
- Main concepts:
  - All coachings have to be pased on a package which has attributes such as duration in weeks, trainings per session, number of trainings per week etc.
  - Additionally, the coachings can be customized with dedicated coaching modules
  - All data for the packages and modules shall be saved in a data base to ease the change process to the application
  - Screens
    - Home screen
    - Func selection
    - Participant master data
    - Package selection
    - Custom module selection Coach and BL
    - Coach selection
    - Starting and ending date
    - Notes for the coaching
    - Overview page
  - Design principles
    - Each screen should be a standalone screen to reduce coupling
    - Design should be based on ttkbootstrap

## User interface
- User stories
  - Participant arrives at welcome talk where the coaching is determined including the coach selection and the selection of a package and modules
  - Later, additional functionality may need to be added. Therefore, the above user journey shall only be one option on the start screen

## Technical specification
- Database tables
  - BLCrew
    - Title
    - FirstName
    - LastName
    - Email
    - Phone
  - Coaches
    - Title
    - FirstName
    - LastName
    - Description
    - Email
    - WebsiteLink
  - Participants
    - Title
    - FirstName
    - LastName
    - Email
    - Phone
  - Packages
    - Name
    - Duration in weeks (DurationInWeeks)
    - Number of training hours (UEs)
    - Sessions per week (SessionsPerWeek)
    - Training hours per session (UEperWeek)
    - Description
    - Training hours given by the Coach (UECoach)
    - Training hours given by BL (UEBL)
  - Modules
    - Name
    - Description
    - MinUEs
    - MaxUEs
    - DefaultOwner
- Libraries
  - tkinter
  - ttkbootstrap
- Classes
  - BLCrew
  - Coach
  - Participant
  - Package
  - Module
  - Coaching

## Testing and security
- Local application only: needs to run on BL managers machines
- Testing through pytest and other unittest modules where needed

## Deployment
- Three environments
  - DEV
  - TST
  - PRD

## Planning
- Dev steps
  - Create three environments
  - Create and fill data base
  - Write classes
  - Design wireframes
  - Develop the app

## Broader context
- Limitations
  - Only locally available
  - Has to be run on local machines of BL crew
  - Design will not be responsive
- Possible extensions
  - Automated time sheets
  - Automated emails based on configured coaching
