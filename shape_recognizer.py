import numpy as np


class ShapeRecognizer:

    def classify(self, stroke):

        if len(stroke) < 10:
            return "line"

        xs = [p[0] for p in stroke]
        ys = [p[1] for p in stroke]

        width = max(xs) - min(xs)
        height = max(ys) - min(ys)

        aspect = width / (height + 1e-5)

        # simple heuristics (MVP version)

        if 0.8 < aspect < 1.2:
            return "circle"

        if aspect > 2:
            return "line"

        if aspect < 0.8:
            return "vertical_shape"

        return "unknown"