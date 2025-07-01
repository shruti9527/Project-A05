# Use an official OpenJDK image
FROM openjdk:17-slim

# Set the working directory
WORKDIR /app

# Copy your Java source code into the container
COPY SimpleCalculator.java .

# Compile the Java source code
RUN javac SimpleCalculator.java

# Run the compiled Java program
CMD ["java", "SimpleCalculator"]
