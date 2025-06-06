import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.io.File;

public class GameLauncher extends JFrame {
    private JTextField playerSpeedField;
    private JTextField rotationSpeedField;
    private JButton runButton;

    public GameLauncher() {
        setTitle("Doom Engine Launcher");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setLocationRelativeTo(null);
        setResizable(false);

        // Create main panel with padding
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new GridLayout(3, 2, 10, 10));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        // Player Speed input
        mainPanel.add(new JLabel("Player Speed (50 = normal):"));
        playerSpeedField = new JTextField("50");
        mainPanel.add(playerSpeedField);

        // Rotation Speed input
        mainPanel.add(new JLabel("Rotation Speed (50 = normal):"));
        rotationSpeedField = new JTextField("50");
        mainPanel.add(rotationSpeedField);

        // Run button
        runButton = new JButton("Run Game");
        runButton.addActionListener(e -> launchGame());
        mainPanel.add(runButton);

        add(mainPanel);
    }

    private void launchGame() {
        try {
            // Get the values from text fields
            String playerSpeed = playerSpeedField.getText();
            String rotationSpeed = rotationSpeedField.getText();

            // Validate inputs
            try {
                double speed = Double.parseDouble(playerSpeed);
                double rotSpeed = Double.parseDouble(rotationSpeed);
                
                if (speed <= 0 || rotSpeed <= 0) {
                    JOptionPane.showMessageDialog(this,
                        "Speed values must be greater than 0",
                        "Invalid Input",
                        JOptionPane.ERROR_MESSAGE);
                    return;
                }
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this,
                    "Please enter valid numbers",
                    "Invalid Input",
                    JOptionPane.ERROR_MESSAGE);
                return;
            }

            // Get the current directory
            File currentDir = new File(".");
            String pythonCommand = "python";
            
            // Try to use python3 if python doesn't work
            try {
                ProcessBuilder checkPython = new ProcessBuilder("python", "--version");
                Process process = checkPython.start();
                if (process.waitFor() != 0) {
                    pythonCommand = "python3";
                }
            } catch (Exception e) {
                pythonCommand = "python3";
            }

            // Create the command to run the Python script
            ProcessBuilder processBuilder = new ProcessBuilder(
                pythonCommand, "launch_game.py",
                "--player-speed", playerSpeed,
                "--rotation-speed", rotationSpeed
            );
            
            // Set the working directory to the current directory
            processBuilder.directory(currentDir);
            
            // Redirect error stream to output stream
            processBuilder.redirectErrorStream(true);
            
            // Start the process
            processBuilder.start();
            
            // Close the launcher window
            dispose();
            
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this,
                "Error launching game: " + ex.getMessage(),
                "Error",
                JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new GameLauncher().setVisible(true);
        });
    }
} 