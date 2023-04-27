# NoteManager


![]()![responsive](https://user-images.githubusercontent.com/66474546/234860253-8c4bc7bc-9cc8-4778-8194-cf3bb136e137.jpg)


# A responsive web apllication were the users can store, update and delete tasks.


## Code Institute Milestone Project 3

## HTML/ CSS/ Python/ Flask / MONGO.db - Backend Development

### Developer: Veronica Preda

# Table Of Content

   -Project Goal
  - Bussnines Goal
  - (ux) User Experience:
       -User Stories
          -First Time Users Goals
          -Returning Users Goals
          -Frequent User Goals
          -Website Owner Goals
       - I want users to: 
   -Design:
       - Theme And Color
   - Wireframe
   - Features
      - Existing Features 
      
   - Technologies:
      - Languages Used
      - Frameworks Libraries 
   - Database Schema
       - Schema
   - Testing
       -Validator Results 
    - Lighthouse
      - Bugs And Errors During Development
    - Deploiment
         - Deploiment to Github Pages
         - Deploiment to Heroku
    
   - Cloning repository:
       - Forking repository:
   - Credits:


# Project Goal 

## The goal of this task app project is to provide a user-friendly platform for individuals or teams to manage their tasks, increase productivity, and improve time management skills by enabling users to easily add, track, and complete tasks. The app should also provide features such as task prioritization, and progress tracking to help users stay organized and on top of their responsibilities.
      
    
# Bussines Goal 

## Increase productivity: The task app can help individuals or teams manage their tasks more efficiently, resulting in increased productivity.
## Improve time management: By providing a platform for users to track and prioritize their tasks, The task app can help users manage their time more effectively. 
## Enhance collaboration: The task app can enable teams to collaborate more effectively by allowing members to assign tasks, set deadlines, and track progress.

# User Expirience 

## Intuitive and easy-to-use interface: The task app has a user-friendly interface that is easy to navigate and understand. Users should be able to quickly add, view, and edit tasks, and access all app features with minimal effort.

## Task prioritization: Users should be able to easily prioritize their tasks, such as by assigning a priority level or due date, to help them focus on the most important tasks and avoid getting overwhelmed.


# User Stories 

  - First Time User 
  
     * As a busy professional, I want to be able to add tasks quickly and easily from my phone, so that I can stay on top of my responsibilities on-the-go.
     * As A first Time User I want to be able to use the app easily
     * As a firt time user I want to be able to easy store and save my tasks
     * As a firt time user i want to easy understand how the app works
     
  - Returning User Goals 
  
    * As a returning user, I want to be able to easily view and edit my existing tasks, so that I can make changes as needed.
    * As a returning user, I want to see my progress on ongoing tasks, so that I can stay motivated and track my productivity.
    * As a returning user, I want to be able to search through my tasks to find specific information or tasks, so that I can easily access what I need.
    * As a returning user, I want to be able to access my task data across multiple devices or platforms, so that I can manage my tasks from anywhere.
    
  
 # Design 
 
   - The task app features a modern and sleek design with a dark blue color scheme that creates a calming and professional aesthetic. The app's layout is designed to be intuitive and user-friendly, with an accordion-style task list that allows users to easily expand and collapse individual tasks for more information or to edit details.

- The search bar is prominently displayed at the top of the app, making it easy for users to quickly find specific tasks or information. The dark blue color scheme is used throughout the app to create a cohesive and consistent visual experience, while also providing a sense of calm and focus to help users stay productive.


# Colors 


![colors](https://user-images.githubusercontent.com/66474546/234869212-bab2769b-20cf-43f8-aa8f-d865195bfa5d.jpg)

# The App responsivnes on Desktop

# Register and Login welcome page 


![welcome page](https://user-images.githubusercontent.com/66474546/234870125-ff8fe64c-0309-42cc-87b4-0381d14aef57.jpg)


# Register page 

![REGISTER PAGE](https://user-images.githubusercontent.com/66474546/234871099-020c0fc1-1935-43b2-a069-8733f7a3018b.jpg)

# Login Page 
![LOGIN PAGE](https://user-images.githubusercontent.com/66474546/234871573-4437243d-1383-497c-9520-4d4b79d9ee3c.jpg)

# Profile Page 

![profile](https://user-images.githubusercontent.com/66474546/234871952-42411a7c-4a07-458d-bd14-2c609450e217.jpg)

# My Tasks Page 

![MY TASKS PAGE](https://user-images.githubusercontent.com/66474546/234872077-f14bc286-2b0f-49a1-be39-57d08d525ee5.jpg)

# Home Page 


![HOMW PAGE](https://user-images.githubusercontent.com/66474546/234872193-440c42e8-29f6-4eed-a891-2d1c030c2b59.jpg)

# New Task Page 

![new  task page](https://user-images.githubusercontent.com/66474546/234872851-480f8cce-f27e-4f9e-90cd-67ddb6fd7fe3.jpg)


# On Mobile 


# Welcome page



![welcome](https://user-images.githubusercontent.com/66474546/234875148-1da034fa-83b1-4c3d-9ac1-d2e4a7349e4b.jpg)

# Register Page 

![REGISTER PAGE](https://user-images.githubusercontent.com/66474546/234875547-7bfeed83-9f50-47b6-b56e-1f328cd247db.jpg)

# Login Page 

![log in](https://user-images.githubusercontent.com/66474546/234875701-1772460d-19ef-4b25-b22a-0b86e29ef588.jpg)

# Profile Page 

![profile](https://user-images.githubusercontent.com/66474546/234875807-eea26daf-6f64-4932-9bdd-b646748a2ee8.jpg)

# My Tasks Page 

![my tasks](https://user-images.githubusercontent.com/66474546/234876008-8a3be101-6289-48d4-994b-29d9e3ed409e.jpg)

# Home Page 

![home](https://user-images.githubusercontent.com/66474546/234876099-bbfc8534-4a63-48c9-a22a-0fa76340f7b5.jpg)

# New Task Page 


![new task](https://user-images.githubusercontent.com/66474546/234876192-e17e4a33-71bc-4cff-a69d-e219b21fc6ab.jpg)

# Features 

- Existing Features 
    
    * Top Navigation Bar For Descktop 
    * Pop up Nav for Mobile
    
- I keept the nav simple for a nice and easy to use feeling



# Technologies

## Languages Used:
   - HTML
   - CSS
   - PYTHON3
   
   
## Frameworks Libraries 

  - Google Fonts
  - Font Awsome 
  - Git
  - Gitpod
  - Github
  - Flask
  - MONGO.DB
  
  
# DATABASE Schema

## The falowing collection have been created

### tasks

 {
  _id: ObjectId,
  title: String,
  description: String,
  due_date: Date,
  completed: Boolean,
  is_urgent: Boolean,
  is_in_progress: Boolean
 }

# app Chart Flow 

![flow chart](https://user-images.githubusercontent.com/66474546/234881074-f6f8839e-63c4-4242-b9ac-fb92c7a221b4.jpg)

# Project Schema 

![project schema](https://user-images.githubusercontent.com/66474546/234881211-928fad74-c230-45c1-b72a-e302ed67c9bf.jpg)



# Testing 
 ## Testing Results 
 
# CSS 
 - The results show no errors 
 
![css](https://user-images.githubusercontent.com/66474546/234882416-c4b94dd4-7fb2-4c1f-93e4-d5858458d37b.jpg)

# HTML

- The validator give me en error as it doesn't reconise the templates
![error](https://user-images.githubusercontent.com/66474546/234882740-98028fd3-baa5-42ef-ba65-323cbe497f0e.jpg)

# Lighthouse 



![lighthouse](https://user-images.githubusercontent.com/66474546/234882919-8f4c3a46-6b46-4bae-b78a-45f1bced3add.jpg)




