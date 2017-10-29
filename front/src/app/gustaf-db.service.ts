import { Show } from './show';
import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable()
export class GustafDbService {

  private showsUrl = 'shows';

  constructor(private http: Http) {}

  getShows(): Promise<Show[]> {
    return this.http.get(this.showsUrl)
              .toPromise()
              .then(response => response.json()._items as Show[])
              .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }

}
