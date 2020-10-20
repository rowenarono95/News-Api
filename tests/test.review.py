import unittest
from app.models import Review
class TestReview(unittest.TestCase):
    def setUp(self):
        self.new_review = Review(12345,"Review for movies","https://image.tmdb.org/t/p/w500/jdjdjdjn","good")
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Review.all_reviews = []
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.title,'Review for movies')
        self.assertEquals(self.new_review.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.review,'good')
    def test_save_review(self):
        '''
        test_save_review test case to test if the review object is saved into
         the review list
        '''
        self.new_review.save_review() # saving the new review
        self.assertEqual(len(Review.all_reviews),1)