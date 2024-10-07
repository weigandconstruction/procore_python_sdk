# RestV10BimPlansGet200ResponseInnerAllOfImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | Base name of the file without its path | [optional] 
**content_type** | **str** | A mime type or a file extension | [optional] 
**url** | **str** | URL to download the attached file. HTTP client should be prepared to follow redirects to successfully download the file. | [optional] 
**height** | **int** | Image height | [optional] 
**width** | **int** | Image width | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_plans_get200_response_inner_all_of_image import RestV10BimPlansGet200ResponseInnerAllOfImage

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimPlansGet200ResponseInnerAllOfImage from a JSON string
rest_v10_bim_plans_get200_response_inner_all_of_image_instance = RestV10BimPlansGet200ResponseInnerAllOfImage.from_json(json)
# print the JSON string representation of the object
print(RestV10BimPlansGet200ResponseInnerAllOfImage.to_json())

# convert the object into a dict
rest_v10_bim_plans_get200_response_inner_all_of_image_dict = rest_v10_bim_plans_get200_response_inner_all_of_image_instance.to_dict()
# create an instance of RestV10BimPlansGet200ResponseInnerAllOfImage from a dict
rest_v10_bim_plans_get200_response_inner_all_of_image_from_dict = RestV10BimPlansGet200ResponseInnerAllOfImage.from_dict(rest_v10_bim_plans_get200_response_inner_all_of_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


