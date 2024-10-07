# RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Segment Item Code | 
**name** | **str** | Segment Item Name | 
**parent_id** | **int** | Parent ID | [optional] 
**sub_job_id** | **int** | Required to create a legacy cost code for a specific sub job | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request import RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest from a JSON string
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_instance = RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_dict = rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest from a dict
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_from_dict = RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsPostRequest.from_dict(rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


