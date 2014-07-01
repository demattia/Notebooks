#ifndef RSAMUONTIME_H
#define RSAMUONTIME_H

struct MuonTime
{
  MuonTime()
    : nDof(0), inverseBeta(0), inverseBetaErr(0),
      freeInverseBeta(0), freeInverseBetaErr(0),
      timeAtIpInOut(0), timeAtIpInOutErr(0),
      timeAtIpOutIn(0), timeAtIpOutInErr(0)
  {}

  /// number of measurements used in timing calculation
  int nDof;

  /// 1/beta for prompt particle hypothesis
  float inverseBeta;
  float inverseBetaErr;

  /// unconstrained 1/beta (time is free)
  float freeInverseBeta;
  float freeInverseBetaErr;

  /// time of arrival at the IP for the Beta=1 hypothesis
  float timeAtIpInOut;
  float timeAtIpInOutErr;
  float timeAtIpOutIn;
  float timeAtIpOutInErr;

  /// To estimate the direction based on timing
  enum Direction { OutsideIn = -1, Undefined = 0, InsideOut = 1 };
  Direction direction() const
  {
    if (nDof<2) return Undefined;
    if ( timeAtIpInOutErr > timeAtIpOutInErr ) return OutsideIn;
    return InsideOut;
  }
};

#endif
