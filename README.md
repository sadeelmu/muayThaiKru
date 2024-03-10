# muayThaiKru

### Description:
The Muay Thai Kru (Training Assistant) is a comprehensive software tool tailored for martial artists, specifically those practicing Muay Thai. By integrating real-time body tracking, sound analysis, and scoring algorithms, this tool provides personalized feedback to users, enabling them to refine their techniques, footwork, and overall performance.

### Technologies Used:
Python: Core programming language for implementing the application logic.
No Kinetic SDK: Enables real-time tracking of body movements, facilitating detailed analysis of technique and footwork. Based on the Xbox kinect body gesture tracking.
WebSockets: Communication protocol used to interface with the No Kinetic system for receiving body tracking data.
PyAudio: Library for sound input capture and analysis, utilized in conjunction with body tracking.
Python Libraries: Additional libraries for data processing, WebSocket connection, , visualization, and user interface development.

### Features:
Real-Time Body Tracking:
  Harnesses the capabilities of the No Kinetic SDK to track the user's movements in real-time, providing detailed feedback on posture, technique, and footwork.
  
Sound-Triggered Analysis:
  Activates sound analysis algorithms only when the body tracking system detects a kick or punch, ensuring precise assessment of technique and sound intensity.

Multi-Factor Scoring System:
  Implements a sophisticated scoring system that evaluates various factors including footwork, technique, and sound intensity, providing holistic feedback to users.

Personalized Feedback Mechanism:
  Offers personalized feedback tailored to each user's strengths and areas for improvement, enhancing their training experience and performance.
