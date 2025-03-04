# NEEM Logging via neem_interface_python
Ah, so you're one of the brave souls ready to dive into the world of logging NEEMs from virtual reality experiments? Well, we admire your courage, and I am writing this tutorial here to help guide you through it with minimal sweat and no tears. Let's get you up and running faster than you can say "**Onomatopoeia**!."

This tutorial is split into two glorious sections:

**Installing RobCog(Unreal Engine v4.27) on Windows** (because who doesn’t love a good challenge?)
**Installing KnowRob on Ubuntu Neotic** (because Linux is secretly your best friend).

Few silent words: Before you dive into the mystical world of RobCog and KnowRob, there are a few things you should know. You should have at least a basic understanding of these:

### Requirements: 
**KnowRob**: The wise oracle of symbolic reasoning and knowledge representation (kind of like your robot’s brain... but much cooler).
**RobCog**: RobCog helps you slay tasks in VR, and when you're done being a VR wizard, it sends a magical scroll (aka REST calls) to KnowRob to log all your epic deeds—because every hero needs a proper record of their conquests, right?
**MongoDB**: A database that stores your data like a giant treasure chest. You don’t have to worry about dragons, though.
**Ontology Modelling**: The mystical art of defining concepts and relationships. Think of it like a map to your robot’s brain.
**Prolog (a smidge)**: You know, just a tiny bit of logic-based magic that will make the robots (and you) feel smarter.
**Flask REST APIs**: You’ll be calling upon these APIs like a wizard casting spells to interact with distant systems. Pretty cool, right?


# **🚀 Setting Up the RobCog on Windows Side – Let’s Go! 🤖**  
---
Follow these steps carefully, and soon you'll be working with VR like a pro!  

#### **Step 1: Install RobCog**  
Head over to the [RobCog Repository](https://github.com/robcog-iai/RobCoG) and follow the step-by-step guide for installation. No shortcuts—trust the process!  

#### **Step 2: Checkout the Right Branch**  
1. Once you've successfully cloned RobCog, switch to the **ApartmentAndPouring** branch. You can find it here: [RobCog ApartmentAndPouring Branch](https://github.com/AbhijitVyas/RobCoG/tree/ApartmentAndPouring).  
Why this branch? Because it includes the latest updates for stable VR hands (thanks, Robin!).  
2. Also while you are at it, checkout [Latest UsemLog Branch: REST_VR_LOGGING_WITH_VR_HANDS](https://github.com/AbhijitVyas/USemLog/tree/REST_VR_LOGGING_WITH_VR_HANDS)
3. Rest of the Plugins should be fine to checkout from standard repositories.

#### **Step 3: Give It a Spin!**  
Try running RobCog and see if everything loads up correctly. If it doesn’t… well, debugging is just part of the fun, right? 😅  

#### **Step 4: Check Time Zones**  
Before diving in, make sure both your Windows and Ubuntu machines are set to the **same time zone**. This is **crucial** for logging accurate timestamps. Otherwise, your logged events might get time-traveled into chaos!  

#### **Step 5: Let’s Explore the RobCog Map! 🔍🎮**  
Now, it's time to explore! Open the **RobCog map** (refer to Figure 1) and start experimenting.  




Alright, time to get hands-on! Follow these steps, and let’s make sure everything is set up correctly.  

##### **Step 5.1: Find the Right Map**  
1. In the **Source Panel**, navigate to:  
   👉 `UVRHands Content/MainContentRH/Maps/Study`  
2. Inside this folder, open one of the maps—let’s go with **8_Pouring Scene**.  

##### **Step 5.2: Explore the Scene**  
Once the map is loaded, take a look around. You should see a **table** with several assets, including:  
- A **cup** ☕  
- **SM_MilkPitcher** 🥛  
- **SM_BigBowl** 🍜  
- And a **Pot** 🍲  

##### **Step 5.3: Select an Object**  
1. Click on the **Pot** (or any other object you want to track).  
2. In the **Details View** (bottom-right side of the screen), search for **"tag"**.  

##### **Step 5.4: Check the Component Tag**  
Look at the **Component Tag**—it should be set as:  
```plaintext
TF;ChildFrameId,Pot;
```  
Here, **"Pot"** is the **URDF link name** of the asset. This is how Unreal knows which object to track and send data to the ROS side.  

#### **Step 5.5: Verify the Mapping**  
Want to check the full mapping details? Take a look at the **Owl and URDF files** for the apartment map:  
- **OWL file:** [iai-apartment.owl](https://github.com/AbhijitVyas/bielefeld_study_neem/blob/master/owl/iai-apartment.owl)  
- **URDF file:** [study_apartment.urdf](https://github.com/AbhijitVyas/bielefeld_study_neem/blob/master/urdf/study_apartment.urdf)  

#### **Bonus Step: Experiment! 🚀**  
Try selecting different objects, checking their tags, and mapping them. The more you explore, the better you'll understand how Unreal communicates with ROS!  

![](https://raw.githubusercontent.com/AbhijitVyas/bielefeld_study_neem/refs/heads/master/images/PouringScene_RobCog.png) Figure 1: Pouring Scene in RobCog

---

### **Let’s Set Up the Several Logger Managers! 🛠️📡**  

Time to fine-tune the logging settings to ensure everything runs smoothly. Follow along step by step and check the figures (Figure 2, 3, & 4) as you go!  

---

### **Step 1: Configure SL_LoggerManager for Semantic Logging**  
🔍 **What we’re doing:** Setting up the KnowRob server connection so we can log semantic triples.  

1. Locate **SL_LoggerManager** in your scene.  
2. In the **Details Panel** (bottom-right side of the screen), find the settings for **KnowRob server**.  
3. Set the **KnowRob Server IP** to your **Ubuntu VM IP address**.  
4. Set the **Port** to `8000`.  

✅ **Double-check:** If everything is set correctly, your logger will be able to communicate with KnowRob. (See Figure 2)  

![](https://raw.githubusercontent.com/AbhijitVyas/bielefeld_study_neem/refs/heads/master/images/SLLoggerManager.png) Figure 2: SL Logger Manager Setting

---

### **Step 2: Set Up TFPublisher for Position Data Logging**  
🔍 **What we’re doing:** Ensuring position data (as **ROS tf messages**) is published correctly.  

1. Place **TFPublisher** in the scene if it’s not already there.  
2. In the **Details Panel**, look for:  
   - **Server IP** → Set this to your **Ubuntu VM IP address**  
   - **Server Port** → Set this to `9090`  
3. Scroll down to the **UTFPublisher** plugin settings. Here, you can set the **Constant Publish Rate** (how frequently tf messages get published).  

✅ **Double-check:** With the right IP and port, your position data will be logged and streamed properly! (See Figure 3)  


![](https://raw.githubusercontent.com/AbhijitVyas/bielefeld_study_neem/refs/heads/master/images/TFPublisher.png) Figure 3: TF Publisher Setting

---

### **Step 3: Update ROSBridge Server Settings**  
🔍 **What we’re doing:** Making sure the Unreal project is correctly connected to ROSBridge.  

1. Go to **Edit** → **Project Settings...**  
2. Navigate to **Engine** → **ROS Settings**  
3. Set **ROSBridge Server Host** to your **Ubuntu VM IP address**  
4. Set **ROSBridge Server Port** to `9090`  

✅ **Double-check:** This ensures your Unreal Engine setup is correctly talking to ROSBridge. (See Figure 4)  


![](https://raw.githubusercontent.com/AbhijitVyas/bielefeld_study_neem/refs/heads/master/images/RosBridgeSetting.png) Figure 4: Ros Bridge Setting

---

### 🎯 **Final Check: Everything Ready?**  
- ✅ **SL_LoggerManager** has the correct **KnowRob IP & Port** (`8000`)  
- ✅ **TFPublisher** is placed in the scene and has the correct **ROSBridge IP & Port** (`9090`)  
- ✅ **Project Settings** are updated for **ROSBridge Server Host & Port**  

🚀 **You’re all set!** Now go ahead and start logging those NEEMs like a pro!  

Let me know if you run into any snags! 🤖🎮




# **🚀 Setting Up the Linux/ROS Side – Let’s Go! 🐧🤖**  

Time to prepare the **ROS** side of things! Follow these steps carefully, and soon your system will be ready to log and process NEEMs.  

---

### **🛠️ Step 1: Install ROS Noetic & Set Up Your Workspace**  
🔹 First, install **ROS Noetic** by following the official guide:  
👉 [ROS Noetic Installation (Ubuntu)](https://wiki.ros.org/noetic/Installation/Ubuntu)  

🔹 Once installed, create a **Catkin workspace** (`catkin_ws`). If you haven’t done this before, follow this guide:  
👉 [Creating a Catkin Workspace](https://wiki.ros.org/catkin/Tutorials/create_a_workspace)  

✅ **Double-check:** After running `source devel/setup.bash`, you should be able to use ROS commands like `roscore`.  

---

### **📦 Step 2: Install KnowRob (Development Branch)**  
🔹 Clone and install the latest **KnowRob** from the development branch:  
👉 [KnowRob Repository](https://github.com/knowrob/knowrob)  

```bash
cd ~/catkin_ws/src
git clone -b dev https://github.com/knowrob/knowrob.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

✅ **Double-check:** Running `rosrun knowrob knowrob.launch` should start the system without errors.  

---

### **🗄️ Step 3: Install MongoDB (v4.2.25)**  
🔹 KnowRob requires a **specific** MongoDB version (`4.2.25`). Follow the instructions in the **KnowRob README** to install it properly.  

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt update
sudo apt install -y mongodb-org=4.2.25
```

✅ **Double-check:** Start MongoDB with `sudo systemctl start mongod` and verify it’s running using `mongo --eval 'db.runCommand({ connectionStatus: 1 })'`.  

---

### **🤓 Step 4: Install SWI-Prolog (rosprolog) (>= 8.2.4)**  
🔹 KnowRob uses **SWI-Prolog**, so you need version **8.2.4 or higher**. Again, follow the instructions in the **KnowRob README** to install it:  

```bash
sudo apt install swi-prolog
swipl --version
```

✅ **Double-check:** Make sure the version is **>=8.2.4** by running `swipl --version`.  

---

### **🔗 Step 5: Clone & Set Up neem_interface-python**  
🔹 This repo handles the REST interface for **NEEMs**. Clone it inside your **catkin workspace**:  

```bash
cd ~/catkin_ws/src
git clone -b rest_interface https://github.com/AbhijitVyas/neem_interface_python.git
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

✅ **Double-check:** The repo should be inside `~/catkin_ws/src` and properly built.  

---

### **🌉 Step 6: Install & Check rosbridge**  
🔹 **rosbridge** is what connects your Unreal Engine setup to ROS via WebSockets. If you haven’t installed it yet, do it now:  

```bash
sudo apt install ros-noetic-rosbridge-server
```

🔹 Check if **rosbridge** is installed:  

```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

✅ **Double-check:** If you see **“[INFO] Rosbridge WebSocket server started on port 9090”**, it’s working! 🎉  

---

### **🎯 Final Check: Is Everything Ready?**  
Before moving on, confirm these are installed and running:  
✅ **ROS Noetic** and **catkin workspace** (`catkin_ws`)  
✅ **KnowRob (dev branch)** installed and running  
✅ **MongoDB v4.2.25** installed and running (`mongod`)  
✅ **SWI-Prolog (>= 8.2.4)** installed (`swipl --version`)  
✅ **neem_interface-python** cloned and built  
✅ **rosbridge** installed and running (`rosbridge_websocket.launch`)  

🚀 **You did it!** Now your ROS setup is ready to receive data from Unreal Engine. Time to log some NEEMs!  


### **🚀 Time to Log Some NEEMs – Let’s Go! 🎮🤖**  

So, you've made it this far—congrats! But now comes the **moment of truth**: making sure everything actually works. 😏  

You'll be running multiple commands, **each in a new terminal**, so get ready to multitask like a pro.  

---

### **🛠 Step 1: Start the Essentials (Open a New Terminal for Each Command!)**  
🔥 **First, let's get the core services running:**  

1️⃣ **Start MongoDB** (because NEEMs need a home! 🏠)  
```bash
sudo systemctl start mongod
```

2️⃣ **Launch KnowRob** (so it can start logging what’s happening in RobCoG)  
```bash
roslaunch knowrob knowrob.launch
```

3️⃣ **Run rosprolog** (the brain behind KnowRob!)  
```bash
rosrun rosprolog rosprolog_commandline.py
```

4️⃣ **Start rosbridge** (so Unreal Engine and ROS can actually talk to each other 📡)  
```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

---

### **📡 Step 2: Start the NEEM Interface REST API**  
🔹 This step ensures that your **NEEMs** can be logged via REST calls.  

1️⃣ **Navigate to the right folder:**  
```bash
cd ~/catkin_ws/src/neem_interface_python/src
```

2️⃣ **Run the bootstrap script:**  
```bash
./bootstrap.sh
```

3️⃣ **Test the API!** Open this URL in your browser:  
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**  

✅ If it says **"Hello, World!"**, you’re golden! 🎉  

---

## **🌍 Step 3: Set Up & Test the ROS Map**  
Okay, now for the **fun** part! You need a **ROS map** that matches your **RobCoG environment**, because KnowRob is a little picky and likes things to be **exact**. 🤓  

1️⃣ **Clone the correct ROS map repo into your workspace:**  
```bash
cd ~/catkin_ws/src
git clone git@github.com:AbhijitVyas/bielefeld_study_neem.git
```

2️⃣ **Launch the map inside RViz:**  
```bash
roslaunch bielefeld_study_neem/launch rviz_launch_map.launch
```

✅ **What should happen?**  
- If you’ve followed everything correctly so far, your RViz map should now be **perfectly aligned** with the RobCoG environment.  
- If things **aren’t** aligning, double-check the URDF files in `bielefeld_study_neem` and **make sure that the tf link name is correctly set in unreal environment as tag for each asset that you want to track!!!**.  

---

## **🎮 Step 4: Fire Up RobCoG & Log Your First NEEM!**  
🚀 Now it’s time to actually **run RobCoG** and start logging events!  

1️⃣ **On the Windows side, start the RobCoG simulation** in either:  
   - **VR mode** (if you have a headset)  
   - **Simulation mode** (for testing without VR)  

2️⃣ **Watch the Linux terminal (where `neem_interface_python` is running).**  
   - You should see **console logs** indicating that an **episode has started**.  

3️⃣ **Perform your experiment in RobCoG.**  
   - Move objects around, perform actions, and interact with the environment.  

4️⃣ **Press the STOP button** when you're done.  
   - This sends a huge **event log** from RobCoG to `neem_interface_python`, where it gets stored as a NEEM.  

---

## **🧠 Step 5: Memorizing Your NEEM (AKA Making It Permanent!)**  
Once you've completed your experiment, it's time to **save** your work inside KnowRob.  

1️⃣ **Go to the rosprolog console.**  

2️⃣ **Load the OWL ontology** for your experiment:  
```prolog
load_owl('~/catkin_ws/src/bielefeld_study_neem/owl/iai-apartment.owl').
```

3️⃣ **Tell KnowRob to memorize the NEEM:**  
```prolog
memorize('~/catkin_ws/src/bielefeld_study_neem/NEEM/').
```

🎉 **BOOM! You just logged your first NEEM!** 🎉  

---

## **🧐 Troubleshooting Tips (Because Something Always Breaks 😂)**  
❌ **MongoDB errors?** → Check if `mongod` is running with `sudo systemctl status mongod`.  
❌ **rosbridge isn’t working?** → Double-check that your **Ubuntu IP address** is correctly set in RobCoG.  
❌ **RViz map isn't aligning?** → Make sure you’re using the correct **URDF & OWL files** for your setup.  
❌ **RobCoG doesn’t send data?** → Ensure both Windows & Ubuntu are using the **same time zone**!  

---

## **🌍 Time to Share Your NEEM with openEASE! 🚀**  

So, you’ve logged a NEEM—nice job! But why keep it to yourself? Let’s **replay it, check if everything looks good, and upload it to openEASE** so others can admire your robot’s skills. 🤖✨  

---

### **🎬 Step 1: Replaying Your NEEM in KnowRob**  

Before you upload anything, let’s make sure it **actually recorded correctly** by replaying it. Here’s how:  

1️⃣ **Load the NEEM from MongoDB into KnowRob**  
```prolog
knowrob_load_neem('').
```
(If everything is working, this should pull your logged NEEM into KnowRob’s memory.)  

2️⃣ **Find the start and end timestamps** in MongoDB:  
   - Open the **tf collection** in MongoDB  
   - Look for the **first and last** `header.stamp` values  
   - Convert them to **epoch time** (UNIX timestamp)  

📝 **Example:**  
Let’s say your first frame is `1674729315` and the last frame is `1674729329`.  

Now, **set the animation goal in tf_plugin**:  
```prolog
tf_plugin:tf_republish_set_goal(1674729315, 1674729329).
```
🎥 **Boom! Your NEEM should now replay in RViz!** 🎉  

---

### **🌟 Step 2: Uploading Your NEEM to openEASE**  

So, does everything look **perfect**? If yes, let’s **share it with the world** on openEASE! 🌍  

🔹 **Make sure your metadata is correct** in the `uploadNeem.py` file.  

🔹 Then, run the following:  
```bash
cd ~/catkin_ws/src/bielefeld_study_neem/
python3 uploadNeem.py
```

---

### **🎉 And That’s It! You’re Officially an openEASE Contributor!**  
✅ You’ve logged a NEEM  
✅ You’ve replayed it successfully  
✅ You’ve uploaded it to openEASE for others to use  

Now sit back, grab a coffee ☕, and admire your robot’s **perfectly logged actions**.  

Or, you know… **go break something and log another NEEM!** 😆

---
## **🎯 Final Thoughts**  
Congratulations! You’ve successfully set up **RobCoG + ROS + KnowRob + NEEM Logging** like a true robotics pro. The process is a marathon and not a sprint, take your sweet time while working with NEEMs, they do not come easy!!! 🤖🔥  

--- 
**Disclaimer**: The following work is not the result of one brilliant mind but rather the collective efforts of several legends. They deserve a proper shoutout, so here goes:

**Andrei Hydu** – The mastermind behind RobCog. Without his vision, we'd probably still be figuring out how to open a virtual fridge.

**Daniel Beßler** – The OG of KnowRob 2.0 (and all its descendants). If knowledge representation had a Hall of Fame, he'd have a whole wing.

**Sascha Jongebloed** – The fearless maintainer of openEASE, NEEMHub, KnowRob, SOMA… Basically, if it has a database and a semantic layer, he's keeping it alive.

**Robin Helmert** – The warrior with a “never say die” attitude who brought stable VR hands into existence. Thanks to him, we now have experimental maps where VR hands don’t randomly teleport to another dimension.

**Manuel Scheibl** – The savior who simplified the nightmare of logging NEEMs with VM and RobCog bridge. Before him, logging was an extreme sport.

**Abhijit Vyas** – The guy who took all of these powerful tools and said, “Alright, let’s log some NEEMs from VR!” (and somehow made it work).

