# MiNiSlack User Stories

## Users

### Sign Up

* As an unregistered and unauthorized user, I want to be able to sign up for the website via a sign-up form.
  * When I'm on the `/signup` page:
    * I would like to be able to enter my first name, last name, email, username, and preferred password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the sign-up form.
      * So that I can seamlessly access the site's functionality
  * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
    * So that I can try again without needing to refill forms I entered valid data into.

### Log in

* As a registered and unauthorized user, I want to be able to log in to the website via a log-in form.
  * When I'm on the `/login` page:
    * I would like to be able to enter my email or username with my password on a clearly laid out form.
    * I would like the website to log me in upon successful completion of the log-in form.
      * So that I can seamlessly access my profile page whiche displays my workspace, channels, and dms.
  * When I enter invalid data on the log-in form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries (except my password).
      * So that I can try again without needing to refill forms I entered valid data into.

### Demo User

* As an unregistered and unauthorized user, I would like an easy to find and clear button on both the `/signup` and `/login` pages to allow me to visit the site as a guest without signing up or logging in.
  * When I'm on either the `/signup` or `/login` pages:
    * I can click on a Demo User button to log me in and allow me access as a normal user.
      * So that I can test the site's features and functionality without needing to stop and enter credentials.

### Log Out

* As a logged in user, I want to log out via an easy to find log out button on the navigation bar.
  * While on any page of the site:
    * I can log out of my account and be redirected to the sign in page.
      * So that I can easily log out to keep my information secure.

## Workspaces

### View Workspaces

* As a logged in user, I want to be able to view all workspaces of which I own or just as a member.
  * When I'm on the `/workspaces` page:
    * I can see my workspace lists I owned or just as a member.
      * Every workspace has a log-in button, so that I can pick one of the workspaces I want to log-in.
  * When I click workspace log-in button, the page will redirect to `/workspaces/:workspaceId` page which will show the workspace details.

### Create New Workspaces

* As a logged in user, I want to able to create a new workspace.
  * When I click on the "CREATE A NEW WORKSPACE" button, I will be redirect to `/workspaces/get-start` page:
    * I can see a "Create a Workspace button", I also can have another option to open a workspace I owned or joined.
    * When I click the "Create a Workspace" button, I will be redirect to `/workspaces/:workspaceId` page:
      * I would like to be able to enter my workspace name, my profile photo, coworkers' email list, and channel name step by step with detailed tips.
      * I would like the website to log me in successful completion of the sign-up steps.
    * When I enter invalid data on the sign-up form:
    * I would like the website to inform me of the validations I failed to pass, and repopulate the form with my valid entries.
    * So that I can try again without needing to refill forms I entered valid data into.

### Updating Workspaces



### Deleting Workspaces



## Channels

### View All Channels

### Create Channels

### Update Channels

### Delete Channels

## Messages

### View All Messages

### Send Messages

### Edit Messages

### Delete Messages

## Reactions

### View All Reactions

### Create Reactions

### Delete Reactions
