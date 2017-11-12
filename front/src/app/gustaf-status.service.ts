import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';

@Injectable()
export class GustafStatusService {

  // Observable string source
  private currentShowSource = new Subject<string>();

  // Observable string streams
  currentShow$ = this.currentShowSource.asObservable();

  setCurrentShow(show: string) {
    this.currentShowSource.next(show);
  }
}
