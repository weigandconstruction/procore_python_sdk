# RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Segment Item Code | [optional] 
**name** | **str** | Segment Item Name | [optional] 
**status** | **str** | Segment Item Status | [optional] 
**sub_job_id** | **int** | Required to update a legacy cost code for a specific sub job | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request import RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest from a JSON string
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request_instance = RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request_dict = rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest from a dict
rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request_from_dict = RestV10ProjectsProjectIdWorkBreakdownStructureSegmentsSegmentIdSegmentItemsIdPatchRequest.from_dict(rest_v10_projects_project_id_work_breakdown_structure_segments_segment_id_segment_items_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


