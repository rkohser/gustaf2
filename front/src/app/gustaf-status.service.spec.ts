import { TestBed, inject } from '@angular/core/testing';

import { GustafStatusService } from './gustaf-status.service';

describe('GustafStatusService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [GustafStatusService]
    });
  });

  it('should be created', inject([GustafStatusService], (service: GustafStatusService) => {
    expect(service).toBeTruthy();
  }));
});
