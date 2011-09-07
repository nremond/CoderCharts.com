#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>      // for sqrt() and pow()
#include <vector>
#include <limits>
#include <time.h>
#include <algorithm>


using namespace std;

class Point2d {
	public : 
		double x, y;
	
	public :	
		Point2d() {x=0; y=0;}
		Point2d(const Point2d &p) {x=p.x; y=p.y;}
		Point2d(double x, double y){
			this->x = x;
			this->y = y;
		}
		
		friend ostream &operator<<(ostream &stream, const Point2d &p);
};

ostream &operator<<(ostream &stream, const Point2d &p) {
			stream << "(" << p.x << "," << p.y << ")";
}

double norm(const Point2d &p1, const Point2d &p2) {
	return std::sqrt( pow(p1.x-p2.x, 2) + pow(p1.y - p2.y, 2)) ;
} 

class Cluster {
	public :
		vector<Point2d> points;
		Point2d centroid;
	
	public :
		Cluster() {}
		Cluster(const Point2d &p) { 
			points.push_back(p); 
			calculateCentroid();
		}
	
	
		double update(vector<Point2d> &points) {
			Point2d old_centroid(centroid);
			this->points.assign(points.begin(), points.end());
			calculateCentroid();
			return norm(old_centroid, centroid);
		}
	
	private :
		void calculateCentroid() {
			centroid.x = 0;
			centroid.y = 0;
			
			for(vector<Point2d>::iterator it = points.begin(); it != points.end(); ++it) {
				centroid.x += it->x;
				centroid.y += it->y;
			}
			
			double n = static_cast<double>(points.size());
			
			centroid.x /= n;
			centroid.y /= n;
		}

};


void kmeans(vector<Point2d> &points, int k, double cutoff, vector<Cluster> &clusters) {
	
	int n = points.size();
	int q = n / k;
	
	//randomize a copy of the points
	vector<Point2d> randomized_points(points);
	random_shuffle(points.begin(), points.end());
	
	//initialize the clusters
	for(int i=0; i<k; ++i){
		//TODO
		clusters.push_back(randomized_points[i]);	
		//clusters.push_back(points[q*i]);
	}

	/*
	cout << "kemans init points";
	for(vector<Cluster>::iterator c = clusters.begin(); c != clusters.end(); ++c) {
		cout << c->centroid << "";
	}
	cout << endl;
	*/
	
	
	while(true) {
		vector<vector<Point2d> > lists(k);
	
		for(vector<Point2d>::iterator p = points.begin(); p != points.end(); ++p) {
			int i = 0;
			int index = 0;
			double smallest_distance = numeric_limits<double>::max();
			for(vector<Cluster>::iterator c = clusters.begin(); c != clusters.end(); ++c) {
		
				double distance = norm(c->centroid, *p);
				//cout << "kmeans::d{" << c->centroid << *p <<"}="<<distance << endl;
				
				if(distance < smallest_distance) {
					smallest_distance = distance;
					index = i;
				}
				
				++i;
			}
			
			lists[index].push_back(*p);
			//cout << "kmeans::lists[" << index << "].push_back(" << *p << ")" << endl;
		}
		
		double biggest_shift = cutoff - (cutoff/10);
		for(int i=0; i<k; ++i) {
			double shift = clusters[i].update(lists[i]);
			biggest_shift = (biggest_shift > shift) ? biggest_shift : shift;
		}

		//cout << "biggest_shift=" << biggest_shift << endl;
		if(biggest_shift < cutoff){
			break;
		} 
	}
	
};

double distance(vector<Point2d> &points, vector<Cluster> &clusters) {
	double D = 0.0;
	for(vector<Point2d>::iterator p = points.begin(); p != points.end(); ++p) {		
		double min = numeric_limits<double>::max();
		for(vector<Cluster>::iterator c = clusters.begin(); c != clusters.end(); ++c) {
				double d = pow(p->x - c->centroid.x, 2) + pow(p->y - c->centroid.y, 2);
				//cout << "distance::d=" << d << endl;
				if(d < min){
					min = d;
				}
		}
		D += min;
	}
	return sqrt(D);
}

int main(int argc, char* argv[]) { 
  
    ifstream file;    
    file.open(argv[1]);
    if (!file) {
        cout << "Unable to open file";
        return 1; // terminate with error
    }
    
	int n;
	file >> n;
	
	vector<Point2d> points(n);
	for(int i=0; i<n; ++i){
		file >> points[i].x;
		file >> points[i].y;
	}
	
	int p;
	file >> p;
	
	vector<int> n_gas_stations(p);
	for(int i=0; i<p; ++i){
		file >> n_gas_stations[i];
	}

    file.close();

	
	int nb_runs = 9;
	if(n == 100) {
		nb_runs = 1;
	}
		
	
	for(int i=0; i<n_gas_stations.size(); ++i) {
		double min_distance = numeric_limits<double>::max();
		vector<Cluster> best_clusters;
		vector<Cluster> clusters;
		
		int g = n_gas_stations[i];

		for(int run=0; run<nb_runs; run++){		
			clusters.clear();
			double cutoff = 0.0005;
			kmeans(points, g, cutoff, clusters);
			
			double d = distance(points, clusters);
			//double d = 1;
			
			//cout << "d=" << d << endl; 
			
			if(d < min_distance) {
				min_distance = d;
				best_clusters = clusters;
				
				//cout << "min_distance=" << d  << endl;
			}
		}		
		
		//	for(vector<Cluster>::iterator c = best_clusters.begin(); c != best_clusters.end(); ++c) {
		for(vector<Cluster>::iterator c = best_clusters.begin(); c != best_clusters.end(); ++c) {
			//cout << c->centroid;
			cout << c->centroid.x << " " << c->centroid.y << " ";
		}
		cout << endl;
	}
		
		
    return 0;
}