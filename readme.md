# How to run

## Create Virtual Environment and Install requirements

##  On the main.py
Inside the main function,
change the parameters of `merger` function call

```python
merger('NFT_Video_Test_050522.mp4', 'OUTPUT-RANDOM_01.jpg', '00:00:03.00', [87, 87, 87], [87, 87, 87])
```

Here
```python
merger(video_file=required, image_file=required, set_image_duration=optional, set_fade_out_color=optional, set_fade_in_color=optional)
```