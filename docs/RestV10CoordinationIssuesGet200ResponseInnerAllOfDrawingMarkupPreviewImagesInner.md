# RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**drawing_revision_id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner import RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner from a JSON string
rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner_instance = RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner.to_json())

# convert the object into a dict
rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner_dict = rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner_instance.to_dict()
# create an instance of RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner from a dict
rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner_from_dict = RestV10CoordinationIssuesGet200ResponseInnerAllOfDrawingMarkupPreviewImagesInner.from_dict(rest_v10_coordination_issues_get200_response_inner_all_of_drawing_markup_preview_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


