# RestV11ProjectsProjectIdUploadsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Reference to the upload that stays valid during the lifecycle of the upload. After uploading to the storage service you will use this reference to associate the upload to another resource. | [optional] 
**url** | **str** | Post the multipart/form-data encoded body with the upload to this URL. Do not attempt to cache or alter the URL in any way or the upload may fail. | [optional] 
**fields** | [**UploadFields**](UploadFields.md) |  | [optional] 
**status** | **str** | Upload status. | [optional] 
**segments** | [**List[SegmentedUploadSegmentsInner]**](SegmentedUploadSegmentsInner.md) | Upload segments. Optional. | [optional] 

## Example

```python
from procore_sdk.models.rest_v11_projects_project_id_uploads_post201_response import RestV11ProjectsProjectIdUploadsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV11ProjectsProjectIdUploadsPost201Response from a JSON string
rest_v11_projects_project_id_uploads_post201_response_instance = RestV11ProjectsProjectIdUploadsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV11ProjectsProjectIdUploadsPost201Response.to_json())

# convert the object into a dict
rest_v11_projects_project_id_uploads_post201_response_dict = rest_v11_projects_project_id_uploads_post201_response_instance.to_dict()
# create an instance of RestV11ProjectsProjectIdUploadsPost201Response from a dict
rest_v11_projects_project_id_uploads_post201_response_from_dict = RestV11ProjectsProjectIdUploadsPost201Response.from_dict(rest_v11_projects_project_id_uploads_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


