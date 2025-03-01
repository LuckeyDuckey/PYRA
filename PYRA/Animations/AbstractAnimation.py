import PYRA.VectorMathClass

class Animation:
    def __init__(self, AnimationParameters):
        self.AnimationParameters = AnimationParameters
        self.AnimationTimeElapsed = 0

    def Lerp(self, StartValue, EndValue, AnimationProgress):
        return StartValue + (EndValue - StartValue) * AnimationProgress

    def GetUpdatedValue(self, AnimationProgress):
        raise NotImplementedError("Child classes must implement GetUpdatedValue()")

    def Update(self, Active, DeltaTime):
        self.AnimationTimeElapsed += DeltaTime if Active else -DeltaTime
        self.AnimationTimeElapsed = max(min(self.AnimationTimeElapsed, self.AnimationParameters.Duration), 0)

        ScaledAnimationTimeElapsed = self.AnimationTimeElapsed / self.AnimationParameters.Duration
        AnimationProgress = self.AnimationParameters.EasingFunction(ScaledAnimationTimeElapsed)

        return self.GetUpdatedValue(AnimationProgress)
