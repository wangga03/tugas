#include <Firebase.h>

#define WIFI_SSID     "hai"
#define WIFI_PASSWORD "wggggw1234"
/* Test Mode (No Authentication) */
#define REFERENCE_URL "https://smile-project-206bd-default-rtdb.asia-southeast1.firebasedatabase.app/"

/* Uncomment the following line for Locked Mode (With Authentication) */
// #define AUTH_TOKEN "YOUR-AUTHENTICATION-CODE"


/* Use the following instance for Test Mode (No Authentication) */
Firebase fb(REFERENCE_URL);

/* Use the following instance for Locked Mode (With Authentication) */
// Firebase fb(REFERENCE_URL, AUTH_TOKEN);

void setup() {
  Serial.begin(115200);

  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);

  /* Connect to WiFi */
  Serial.println();
  Serial.println();
  Serial.print("Connecting to: ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print("-");
    delay(500);
  }

  Serial.println();
  Serial.println("WiFi Connected");
  Serial.println();
}

void loop() {
  int retrievedInt = fb.getInt("state/smile_status");
  Serial.print("Retrieved Int:\t\t");
  Serial.println(retrievedInt);

  if(retrievedInt == 1){
    digitalWrite(12, HIGH);
    digitalWrite(13, LOW);
  }else{
    digitalWrite(12, LOW);
    digitalWrite(13, HIGH);

  }
}
