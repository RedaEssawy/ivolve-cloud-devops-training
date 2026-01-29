# Objective
Configure Jenkins with role-based authorization to control user access to jobs, views, and administrative functions based on user roles.

# Concepts Covered
- Jenkins security realm configuration
- Role-based authorization strategy
- Matrix-based security
- User and group management
- Project-based matrix authorization\

# Prerequisites
- Jenkins installed and accessible
- Admin access to Jenkins
- Role-based Authorization Plugin installed
- Basic understanding of Jenkins security

# Steps

## Step 1: Install Required Plugins

First, ensure you have the necessary plugins installed:

1. Go to **Manage Jenkins → Manage Plugins**

2. In the **Available** tab, search for and install:

    - **Role-based Authorization Strategy**

![Alt Text](assets/images/role-based-plugin.png)
![Alt Text](assets/images/role-based-installed.png)

    - **Matrix Authorization Strategy Plugin** (if not included)

3. Restart Jenkins if prompted

![Alt Text](assets/images/restart-jenkins.png)

## Step 2: Enable Role-based Strategy

<pre>
```# Access Jenkins via browser (usually http://localhost:8080)
# Or configure via Jenkins CLI if available```
</pre>

Web UI Steps:

1. Go to **Manage Jenkins → Configure Global Security**
2. Under **Authorization**, select **Role-Based Strategy**
3. Click **Save**

## Step 3: Create Users

Web UI Method:
1. Go to **Manage Jenkins → Manage Users**
2. Click **Create User**
3. Create:
    - **Username**: `user1`
    - **Password**: `user1pass`
    - **Full name**: `User One`
    - **Email**: `user1@example.com`
4. Repeat for `user2` with password `user2pass`

![Alt Text](assets/images/user1&user2.png)

## Step 4: Configure Global Roles

Go to **Manage Jenkins → Manage and Assign Roles → Manage Roles**
**Global Roles:**

1. Click **Add Role**
2. Create roles with the following permissions:

**admin Role:**
- Role Name: `admin`
- Pattern: `.*`
- Permissions: Select **All** (or at minimum):
    - Overall: Administer
    - Overall: Read
    - Agent: Create, Delete, Configure, Connect, Disconnect
    - Job: Create, Delete, Configure, Build, Cancel, Read
    - Run: Delete, Update
    - View: Create, Delete, Configure, Read
    - SCM: Tag

**read-only Role:**
- Role Name: `read-only`
- Pattern: `.*`
- Permissions:
    - Overall: Read
    - Job: Read 
    - View: Read 
    - Metrics: View

![Alt Text](assets/images/create-roles.png)

## Step 5: Assign Global Roles to Users

Go to **Manage Jenkins → Manage and Assign Roles → Assign Roles**

**Global Roles Assignment:**

1. Find the table with users/groups
2. Assign roles:
    - `user1`: Check **admin** role
    - `user2`: Check **read-only** role
    - `authenticated`: Check **read-only** role (for all logged-in users)
    - `anonymous`: Leave empty or assign minimal read if needed
3. Click **Save**

![Alt Text](assets/images/assign-users.png)

## Step 6: Test Role Assignments

Log out and test each user:

**Test as user1 (admin):**

1. Log in as user1/user1pass
2. Verify you can:
    - Access Manage Jenkins
    - Create new jobs
    - Delete jobs
    - Configure system settings

![Alt Text](assets/images/user1-test.png)

**Test as user2 (read-only):**

1. Log in as user2/user2pass
2. Verify you can:
    - View jobs (if any exist)
    - Cannot create new jobs
    - Cannot access Manage Jenkins
    - Cannot configure jobs

![Alt Text](assets/images/user2-test.png)