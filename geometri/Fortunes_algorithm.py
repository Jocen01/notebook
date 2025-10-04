import heapq
import math
from collections import namedtuple

# Define a simple point class for easier referencing
Point = namedtuple('Point', ['x', 'y'])

class Event:
    def __init__(self, x, point=None, arc=None, is_site=True):
        self.x = x  # x-coordinate of sweep line
        self.point = point  # Point object
        self.arc = arc  # Arc object (for circle events)
        self.is_site = is_site  # True for site event, False for circle event
        self.valid = True  # For circle events that might become invalid

    def __lt__(self, other):
        # Events are primarily sorted by x-coordinate (sweep line position)
        # For same x, site events come before circle events
        if abs(self.x - other.x) > 1e-9:
            return self.x < other.x
        return self.is_site > other.is_site

class Arc:
    def __init__(self, site):
        self.site = site  # Site (Point object) that defines this arc
        self.prev = None  # Previous arc in beach line
        self.next = None  # Next arc in beach line
        self.event = None  # Circle event associated with this arc
        # Edges connected to this arc's breakpoints
        self.left_edge = None
        self.right_edge = None

class Edge:
    def __init__(self, start, site1, site2):
        self.start = start  # Starting point of the edge
        self.end = None  # Ending point (to be determined)
        self.site1 = site1  # Left site
        self.site2 = site2  # Right site
        # Direction vector for the edge (perpendicular to the line connecting sites)
        dx = site2.x - site1.x
        dy = site2.y - site1.y
        # Normalize and rotate 90 degrees
        length = math.sqrt(dx*dx + dy*dy)
        self.direction = Point(dy/length, -dx/length)

class FortuneAlgorithm:
    def __init__(self, sites):
        # Convert input sites to Point objects
        self.sites = [Point(x, y) for x, y in sites]
        self.event_queue = []
        self.beachline = None
        self.edges = []
        self.triangles = []
        self.vertices = []  # Voronoi vertices (circumcenters)
        self.processed_triangles = set()  # Track processed triangles to avoid duplicates
        
        # Initialize event queue with site events
        for site in self.sites:
            heapq.heappush(self.event_queue, Event(site.x, point=site))
        
        # Bounding box for clipping edges
        self.bounding_box = self._compute_bounding_box()
    
    def _compute_bounding_box(self):
        """Compute a bounding box for the diagram with some padding."""
        min_x = min(site.x for site in self.sites)
        max_x = max(site.x for site in self.sites)
        min_y = min(site.y for site in self.sites)
        max_y = max(site.y for site in self.sites)
        
        # Add padding
        padding = max(max_x - min_x, max_y - min_y) * 0.1
        return (min_x - padding, min_y - padding, max_x + padding, max_y + padding)
    
    def process(self):
        """Process all events to construct the Voronoi diagram."""
        while self.event_queue:
            event = heapq.heappop(self.event_queue)
            
            if event.is_site:
                self._handle_site_event(event)
            elif event.valid:  # Only process valid circle events
                self._handle_circle_event(event)
    
    def _handle_site_event(self, event):
        """Handle a site event: insert a new arc into the beachline."""
        pass
    
    def _handle_circle_event(self, event):
        """Handle a circle event: remove an arc from the beachline."""
        pass
    
    def _find_arc_above(self, x, sweep_y):
        """Find the arc in the beachline above the given point."""
        arc = self.beachline
        while arc:
            # Calculate x coordinates of breakpoints
            if arc.next:
                # Check if point is before the right breakpoint
                next_x = self._breakpoint(arc.site, arc.next.site, sweep_y)
                if x < next_x:
                    return arc
            else:
                return arc  # Last arc
            arc = arc.next
        return self.beachline  # Fallback, should not reach here
    
    def get_delaunay_triangulation(self):
        """Get the Delaunay triangulation as a list of triangles."""
        return self.triangles
    
    def get_voronoi_edges(self):
        """Get the Voronoi diagram as a list of edges."""
        return self.edges


# Example Usage
sites = [(1, 5), (3, 6), (7, 2), (9, 4)]
fortune = FortuneAlgorithm(sites)
fortune.process()

# Print triangulation results
triangles = fortune.get_delaunay_triangulation()
print("\nDelaunay triangles:")
for triangle in triangles:
    print(triangle)

# Print Voronoi diagram results
voronoi_edges = fortune.get_voronoi_edges()
print("\nVoronoi edges:")
for edge in voronoi_edges:
    print(edge)