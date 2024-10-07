# Image


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Image ID | [optional] 
**url** | **str** | Image url | [optional] 
**size** | **int** | Image size | [optional] 
**filename** | **str** | Image file name | [optional] 
**description** | **str** | Image description | [optional] 
**thumbnail_url** | **str** | Image thumbnail url | [optional] 
**taken_at** | **datetime** | Image taken at | [optional] 
**created_at** | **datetime** | Image created at | [optional] 
**updated_at** | **datetime** | Image updated at | [optional] 
**location** | [**Location7**](Location7.md) |  | [optional] 
**image_category_name** | **str** | Image Category Name | [optional] 
**image_category_id** | **int** | Image Category ID | [optional] 
**permanently_deleted** | **bool** | Image permanent deletion status | [optional] 
**private** | **bool** | Image private status | [optional] 
**starred** | **bool** | Image starred status | [optional] 
**width** | **int** | Image width | [optional] 
**height** | **int** | Image height | [optional] 
**image_category_private** | **bool** |  | [optional] 
**origin_id** | **int** |  | [optional] 
**daily_log_header_id** | **int** |  | [optional] 
**gps_lat** | **str** |  | [optional] 
**gps_long** | **str** |  | [optional] 
**uploader** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 
**trades** | [**List[Trade2]**](Trade2.md) |  | [optional] 
**comments_count** | **int** | the number of comments on this image | [optional] 

## Example

```python
from procore_sdk.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print(Image.to_json())

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_from_dict = Image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


