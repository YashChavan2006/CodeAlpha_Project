import numpy as np

class Sort:
    def __init__(self):
        self.id_count = 0
        self.objects = {}

    def update(self, detections):
        results = []

        for det in detections:
            x1, y1, x2, y2, conf = det

            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)

            found = False
            for obj_id, (px, py) in self.objects.items():
                if abs(cx - px) < 50 and abs(cy - py) < 50:
                    self.objects[obj_id] = (cx, cy)
                    results.append([x1, y1, x2, y2, obj_id])
                    found = True
                    break

            if not found:
                self.objects[self.id_count] = (cx, cy)
                results.append([x1, y1, x2, y2, self.id_count])
                self.id_count += 1

        return results