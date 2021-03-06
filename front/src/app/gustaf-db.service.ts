import { Show } from './show';
import { Episode } from './episode';
import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class GustafDbService {

  private showsUrl = 'shows';
  private episodesUrl = 'episodes';

  constructor(private http: Http) {}

  getShows(): Promise<Show[]> {
    return this.http.get(this.showsUrl)
              .toPromise()
              .then(response => response.json()._items as Show[])
              .catch(this.handleError);
  }

  getEpisodesPerShow(show_id: string): Promise<Episode[]> {

    return this.http.get(this.episodesUrl,
              {
                params: {
                'where': '{"title":"' + show_id + '"}',
                'sort': 'episode'
                }
              }
              )
              .toPromise()
              .then(response => response.json()._items as Episode[])
              .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

}
