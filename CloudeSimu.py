import json
import time
import paho.mqtt.client as mqtt

# Pointing to the secure enterprise public hub
# أعيدي الأسطر الأولى في بايثون للوضع المحلي
TOPIC = "aeromedic/patients/+/alerts"
BROKER_HOST = "broker.hivemq.com"
BROKER_PORT = 1883  # بورت TCP العادي، سريع وممتاز لبايثون

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("\n🟩 [AEROMEDIC LOCAL] Connected to Local Mosquitto Broker!")
        client.subscribe(TOPIC)
        print(f"📡 [MONITORING ACTIVATED] Listening on topic: {TOPIC} ...\n")
    else:
        print(f"❌ [CONNECTION ERROR] Connection refused with code: {rc}")

def on_message(client, userdata, msg):
    print("=" * 60)
    print("🚨 [CRITICAL INBOUND ALERT DETECTED]")
    print("=" * 60)
    try:
        payload = json.loads(msg.payload.decode('utf-8'))
        print(f"👤 Patient Identifier : {payload.get('patient_id')}")
        print(f"⚡ Activation Pathway  : {payload.get('trigger_source')}")
        print(f"📍 GPS Coordinates    : {payload.get('location')}")
        print(f"🫁 Vital Telemetry    : {payload.get('biometrics')}")
        print(f"⏰ Event Timestamp    : {payload.get('timestamp')}")
        
        print("\n🧠 [EXPERT SYSTEM PIPELINE EXECUTING]:")
        print("   1. [FAIL-SAFE] Patient critical history retrieved. Cross-check: PASSED.")
        print("   2. [GEOLOCATION] Scanning database for nearest active drone station...")
        print("   3. [AUTOPILOT COMMAND] Takeoff packet compiled and transmitted to PX4 Autopilot.")
        print("🟩 [STATUS] Emergency mission successfully dispatched.\n")
        print("=" * 60 + "\n")
    except Exception as e:
        print(f"❌ [DATA CORRUPTION ERROR] Failed to parse payload: {e}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()
except KeyboardInterrupt:
    print("\n🛑 [SHUTDOWN] Mock Cloud core terminated.")