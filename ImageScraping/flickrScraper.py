from flickrapi import FlickrAPI


def search(image, per_page):
	FLICKR_PUBLIC = '98da0895f10194748930761fe0aa65b6'
	FLICKR_SECRET = 'ff80d6c6fe1fa9c8'

	flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
	extras='url_o'

	image = flickr.photos.search(text = image, per_pages = per_page, extras = extras)
	photos = image['photos']
	return photos
	



    





