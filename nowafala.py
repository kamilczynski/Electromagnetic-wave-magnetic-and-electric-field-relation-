from manim import *

class EMWave3D(ThreeDScene):
    def construct(self):
        # Set up the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Parameters for the wave
        wave_length = 4
        amplitude = 1
        wave_speed = 0.5  # Slower wave speed for longer animation
        num_arrows = 20  # Number of arrows to display
        animation_duration = 20  # Total duration of the animation in seconds

        # Create the electric field (E) and magnetic field (B)
        electric_field = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t,
                amplitude * np.sin(2 * PI * (t / wave_length - self.time * wave_speed)),
                0
            ]),
            color=RED,
            t_range=[-4, 4]
        ))

        magnetic_field = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t,
                0,
                amplitude * np.cos(2 * PI * (t / wave_length - self.time * wave_speed))
            ]),
            color=BLUE,
            t_range=[-4, 4]
        ))

        # Create arrows for the electric field
        electric_arrows = always_redraw(lambda: VGroup(*[
            Arrow(
                start=np.array([x, 0, 0]),
                end=np.array([
                    x,
                    amplitude * np.sin(2 * PI * (x / wave_length - self.time * wave_speed)),
                    0
                ]),
                color=RED,
                buff=0,
                stroke_width=2,
                tip_length=0.2,
                max_tip_length_to_length_ratio=0.3
            )
            for x in np.linspace(-4, 4, num_arrows)
        ]))

        # Create arrows for the magnetic field
        magnetic_arrows = always_redraw(lambda: VGroup(*[
            Arrow(
                start=np.array([x, 0, 0]),
                end=np.array([
                    x,
                    0,
                    amplitude * np.cos(2 * PI * (x / wave_length - self.time * wave_speed))
                ]),
                color=BLUE,
                buff=0,
                stroke_width=2,
                tip_length=0.2,
                max_tip_length_to_length_ratio=0.3
            )
            for x in np.linspace(-4, 4, num_arrows)
        ]))

        # Animate the fields and arrows
        self.add(electric_field, magnetic_field, electric_arrows, magnetic_arrows)
        self.begin_ambient_camera_rotation(rate=0.1)  # Slower camera rotation
        self.wait(animation_duration)  # Longer animation duration
        self.stop_ambient_camera_rotation()

# Render the animation
if __name__ == "__main__":
    scene = EMWave3D()
    scene.render()

    # To use:
    # manim -pqk C:\Users\topgu\PycharmProjects\obrazowanie\venv\nowafala.py EMWave3D