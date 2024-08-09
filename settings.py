class Settings:
    """Клас для зберігання всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Налаштування корабля
        self.ship_speed = 1.5

        # Налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
