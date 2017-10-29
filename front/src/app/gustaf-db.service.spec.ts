import { TestBed, inject } from '@angular/core/testing';

import { GustafDbService } from './gustaf-db.service';

describe('GustafDbService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GustafDbService]
    });
  });

  it('should be created', inject([GustafDbService], (service: GustafDbService) => {
    expect(service).toBeTruthy();
  }));
});
