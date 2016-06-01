from apiclient.discovery import build
import locale, re, API_KEY

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

DEVELOPER_KEY = API_KEY.key
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def run_query(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=50,
        type="video",

    ).execute()

    video_ids = []
    for search_result in search_response.get("items", []):
        video_ids.append(search_result["id"]["videoId"])
    video_response = youtube.videos().list(
        id=','.join(video_ids),
        part='contentDetails, statistics'
    ).execute()

    results = []

    for (search_result, video_result) in zip(search_response.get("items", []), video_response.get("items", [])):
        video = {"title": search_result["snippet"]["title"], "description": search_result["snippet"]["description"],
                 "videoId": search_result["id"]["videoId"]}
        time = re.search(r'PT(\d+H)?(\d+M)?(\d+S)?',video_result["contentDetails"]["duration"])
        video["duration"] = ':'.join([time.group(i)[:-1].zfill(2) for i in range(1,4) if time.group(i)])
        video["viewCount"] = locale.format("%d", int(video_result["statistics"]["viewCount"]), grouping=True)
        results.append(video)

    return results


def get_related_videos(videoId):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        part="id,snippet",
        maxResults=10,
        type="video",
        relatedToVideoId=videoId

    ).execute()

    video_ids = []
    for search_result in search_response.get("items", []):
        video_ids.append(search_result["id"]["videoId"])
    video_response = youtube.videos().list(
        id=','.join(video_ids),
        part='contentDetails, statistics'
    ).execute()

    results = []

    for (search_result, video_result) in zip(search_response.get("items", []), video_response.get("items", [])):
        video = {"description": search_result["snippet"]["description"],
                 "videoId": search_result["id"]["videoId"]}
        video_title = search_result["snippet"]["title"]
        if len(video_title) > 50:
            video_title = video_title[:50] + "..."
        video["title"] = video_title
        time = re.search(r'PT(\d+H)?(\d+M)?(\d+S)?',video_result["contentDetails"]["duration"])
        video["duration"] = ':'.join([time.group(i)[:-1].zfill(2) for i in range(1,4) if time.group(i)])
        video["viewCount"] = locale.format("%d", int(video_result["statistics"]["viewCount"]), grouping=True)
        results.append(video)

    return results
