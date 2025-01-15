# Smart-Memory-Manager

__Project Overview__ -

Mobile devices often face resource constraints such as limited memory and storage, which can affect the performance of mobile applications. The **Furthest in the Future Paging Algorithm** is a strategy that helps in efficiently managing memory by predicting which apps or data will be required next. The algorithm keeps the most likely-to-be-used apps in memory while evicting less likely ones, ensuring a smoother user experience and better memory management.

This project demonstrates the use of the Furthest in the Future Paging Algorithm to optimize memory management in mobile devices, improving app performance, reducing battery consumption, and optimizing storage space.

__Key Features__ -
- **Predictive Memory Management:** The algorithm predicts which applications are most likely to be used next and keeps them in memory while evicting others.
- **Efficient Cache Management:** Only a limited number of apps are kept in memory based on predicted future usage, minimizing memory overload.
- **Performance Enhancement:** Reduces delays in app switching and optimizes memory utilization, leading to faster app performance.
- **Battery Optimization:** By managing memory efficiently, it also helps in reducing the energy consumed by apps that would otherwise stay loaded unnecessarily.
- **Easy Integration:** Designed to be integrated into mobile applications and operating systems for automatic memory management.

__Technologies Used__ -
- **Python:** For implementing the Furthest in the Future Paging Algorithm and testing the memory management solution.
- **Heapq (Priority Queue):** For managing the cache and tracking future app usage.
- **Collections (Deque, defaultdict):** For handling future predictions efficiently and managing the queue of future app uses.
- **Mobile Development Frameworks (Android/iOS):** This project can be integrated with Android (Java/Kotlin) or iOS (Swift) for real-time memory optimization in mobile apps.

__How It Works__ -
1. **Input Data:** The algorithm receives a sequence of app usage requests (represented as integers or app identifiers).
2. **Memory Management:** 
   - The algorithm maintains a set to simulate the device’s memory cache (with a size limit).
   - As each app is requested, the algorithm checks if it is already in memory.
   - If the app is not in memory, a page fault occurs, and the app is added to memory.
   - If the memory is full, the algorithm identifies the app that will be needed furthest in the future and evicts it from memory.
3. **Cache Eviction:** The cache eviction is based on which app’s next usage will occur the furthest in the future, ensuring that the memory is used for the most likely-to-be-needed apps.
4. **Output:** The number of page faults (i.e., how many times an app had to be loaded into memory) is returned.
