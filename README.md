#Error Detection & Correction Simulation (Python · Client–Server–Client)

## Project on Error Detection and Correction Modeling

This project provides a complete simulation of data transmission over an unreliable channel, demonstrating five error-detection methods and one error-correction method (Hamming Code) within a **Client 1 $\rightarrow$ Server $\rightarrow$ Client 2** architecture.

---

## Implemented Error Control Methods

All required methods are implemented in the `control.py` module and successfully tested for detecting errors introduced by the server.

| Method | Description | Implementation Details |
| :--- | :--- | :--- |
| **✔ PARITY** | Parity Bit. | Detects single-bit errors. |
| **✔ 2D PARITY** | 2D Parity (Matrix Parity). | Detects single and many burst errors. |
| **✔ CRC16** | Cyclic Redundancy Check. | Highly reliable error detection, using the **CRC-16 IBM** polynomial. |
| **✔ CHECKSUM16** | Checksum (IP Checksum). | Calculates the 16-bit checksum. |
| **✔ HAMMING** | Hamming Code. | **Generates check bits** for error detection. *(Per assignment requirements, correction logic is not implemented)*. |

---

## Architecture and Functionality

The project is divided into four self-contained modules operating via the TCP/IP network protocol.

### 1. Client 1 (`client1.py`)

* **Data Sender.** The transmission initiator.
* Accepts **DATA** (text) and **METHOD (1-5)** from the user.
* Forms the packet: `DATA|METHOD|CONTROL_INFORMATION`.
* Sends the packet to the Server (Port: 5000).

### 2. Server (`server.py`)

* **Full Corruption Engine.** An intermediary node simulating channel noise.
* Implements **7 error injection methods** (including `char_sub`, `char_del`, `burst`).
* **Enhancement:** For bit-level errors (`bit_flip`, `multi_flip`, `burst`), data is first converted to a bit string, corrupted, and then restored to characters, ensuring precise simulation.
* Forwards the **corrupted data** and the **original control code** to Client 2 (Port: 5001).

### 3. Client 2 (`client2.py`)

* **Receiver + Error Checker.**
* Receives the packet and recalculates the control code based on the potentially corrupted data.
* **Comparison:** Compares the recalculated code with the received code.
* Outputs a formatted log and the **status** (`DATA CORRECT` or `DATA CORRUPTED`).

---

## How to Run Project

Three separate terminals are required for testing.

1.  **Terminal 1 (Receiver):** `python client2.py`
2.  **Terminal 2 (Server):** `python server.py`
3.  **Terminal 3 (Sender):** `python client1.py`

*Input:* Enter **DATA** (e.g., `Example`) and **METHOD** (1-5).
