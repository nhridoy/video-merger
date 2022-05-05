from moviepy.editor import *


def merger(input_video, input_image, image_duration='00:00:03.00', fade_out_color=[87, 87, 87], fade_in_color=[87, 87, 87]):
    video = VideoFileClip(input_video)
    image = ImageClip(input_image).set_duration(image_duration)  # H:M:S:MS

    def crop(clip):
        clip = clip.crop(x1=420, width=1080)
        return clip

    image = image.subclip(0, image.end).fx(vfx.fadeout, .5, final_color=fade_out_color)
    video = video.subclip(0, video.end).fx(vfx.fadein, .5, initial_color=fade_in_color)

    combine = concatenate_videoclips([image, crop(video)])

    combine.write_videofile(f"{input_video.split('.')[0]}_{input_image.split('.')[0]}_output.mp4")


if __name__ == "__main__":
    merger('NFT_Video_Test_050522.mp4', 'OUTPUT-RANDOM_10.jpg', '00:00:03.00', [87, 87, 87], [87, 87, 87])
