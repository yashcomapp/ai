import { MetadataRoute } from 'next';

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'YASHCOM-LOS',
    short_name: 'YASHCOM-LOS',
    description: 'YASHCOM Learning Outcome System — exams, practice, and progress tracking.',
    start_url: '/',
    scope: '/',
    display: 'standalone',
    orientation: 'any',
    background_color: 'rgb(30, 58, 138)',
    theme_color: 'rgb(30, 58, 138)',
    icons: [
      {
        src: '/icons/icon-192.png?v=2',
        sizes: '192x192',
        type: 'image/png',
        purpose: 'any'
      },
      {
        src: '/icons/icon-512.png?v=2',
        sizes: '512x512',
        type: 'image/png',
        purpose: 'any'
      },
      {
        src: '/icons/icon-512-maskable.png?v=2',
        sizes: '512x512',
        type: 'image/png',
        purpose: 'maskable'
      },
      {
        src: '/icons/badge-96.png?v=4',
        sizes: '96x96',
        type: 'image/png',
        purpose: 'monochrome'
      }
    ]
  };
}
