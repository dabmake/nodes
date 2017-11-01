#include <ros.h>
#include <std_msgs/Empty.h>
#include <geometry_msgs/Twist.h>
#define EN1 9
#define EN2 6
#define PH1 8
#define PH2 7
#define SLEEP 12


ros::NodeHandle  nh;

void velCallback(const geometry_msgs::Twist& cmd_msg){
  digitalWrite(13, HIGH-digitalRead(13));   // blink the led
  digitalWrite(PH1, 1);
  digitalWrite(PH2, 1);
  digitalWrite(SLEEP, 1);
  
  analogWrite(EN1, cmd_msg.linear.x);
  analogWrite(EN2, cmd_msg.linear.y); 
  //cmd_msg.linear.z
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", velCallback);

//ros::Subscriber<std_msgs::Empty> sub("toggle_led", &messageCb );

void setup()
{ 
  pinMode(13, OUTPUT);
  pinMode(PH1, OUTPUT);
  pinMode(PH2, OUTPUT);
  pinMode(SLEEP, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
