import cv2
import numpy as np


def create_video(text):

    # Указываем размеры для видео
    width, height = 100, 100

    # Продолжительность видео
    duration = 3

    # FPS, что тут еще сказать
    fps = 30

    # Задаем параметры для видео
    out = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Создаем кадр
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Начальные координаты для бегущей строки
    x, y = width, height // 2

    # Установим параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX # Поддержка кириллицы
    font_scale = 0.5
    font_thickness = 1
    font_color = (255, 255, 255)  # Белый цвет текста

    # Найдем размеры бегущей строки
    message_size = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Вычислим скорость, с которой необходимо двигать строку (о да, физика)
    v = round( (width + message_size[0][0]) / (duration * fps) )

    # Двигаем строку каждый кадр
    for i in range(duration * fps):

        # Очистка кадра
        frame.fill(0)

        # Двигаем строку с найденной скоростью
        x -= v

        # Добавляем текст
        cv2.putText(frame, text, (x, y), font, font_scale, font_color, font_thickness)

        # Записываем кадр
        out.write(frame)

    # Закрываем видеопоток
    out.release()


if __name__ == "__main__":

    message = input("Введите бегущую строку: ")

    create_video(message)