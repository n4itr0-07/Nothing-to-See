function ytdownload {
    param (
        [Parameter(Mandatory = $true)]
        [string]$url
    )
    yt-dlp -f "bv*+ba/best" -S "res,ext:mp4" -N 4 `
    -o "%(title)s.%(ext)s" `
    -P "C:\Users\Salik\Videos\yt-dlp-downloads" `
    $url
}
