import os

from detection import RNNDetector
from domain.track import Track
from utils import file_utils


class RNNValidator:

    def __init__(self, detector:RNNDetector):
        self.detector = detector

    def load_annotation_file(self, json_file_path :str) -> dict :
        return file_utils.read_json_file(json_file_path)

    def map_annotation_elmt_to_prediction_ndx(self, media_file_annotation:dict) -> [(int,int)] :
        ''' Get the related prediction sequence(int,int) list of the media file positive annotation

        :param Media_file_annotation: Json representation of the annotated file
        :return: A List of (int, int) where each tuple represent the sequence of the related prediction 'start index' and 'end index'
        '''
        track = Track()


        # self.compute_prediction_metrics(
        #         map(lambda track_elmt: track.map_annotation_set_to_prediction_ndxes(track_elmt), all_annotations.get("tracks"))
        # )
        # return [ track.map_annotation_set_to_prediction_ndxes(track_elmt) for track_elmt in media_file_annotation.get("tracks")]
        l = [(int,int)]
        l.append(track.map_annotation_set_to_prediction_ndxes(track_elmt) for track_elmt in media_file_annotation.get("tracks"))
        return l

    def compute_prediction_metrics(self, positive_prediction_ndxes = [(int,int)]) -> (float, float, float):
        for biNdx in positive_prediction_ndxes :
            print(f"start:{biNdx[0]} - {biNdx[1]}")
            # print(f"start:{biNdx[1].__class__}")
        return (1,2,3)

if __name__ == '__main__' :
    detector = RNNDetector()
    validator = RNNValidator(detector)
    all_annotations = validator.load_annotation_file( os.path.abspath(os.path.join(os.path.dirname(__file__), "media-annotation/SWIFT_20000101_022052.json")) )
    list_of_tuples = validator.map_annotation_elmt_to_prediction_ndx(all_annotations)
    validator.compute_prediction_metrics(list_of_tuples)
    # global_score, local_score = detector.predict_on_wav(os.path.abspath(os.path.join(os.path.dirname(__file__), "media/SWIFT_20190723_050006.wav"))) # NB: Check that loaded wav file actually exists on your disk
    # print(f"Golbal score: {global_score}  -  Localscore: {local_score}")