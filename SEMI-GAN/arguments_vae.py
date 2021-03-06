import argparse

def get_args():
    parser = argparse.ArgumentParser(description='SEMI')
    parser.add_argument('--date', type=str, default='', help='(default=%(default)s)')
    parser.add_argument('--dataset', default='2020_LER_20200804_V006.xlsx', type=str, required=False,
                        choices=['LER_data_20191125.xlsx',
                                 'LER_data_20191107.xlsx',
                                 '2020_LER_20200529_V004.xlsx',
                                '2020_LER_20200804_V006.xlsx'], 
                        help='(default=%(default)s)')
    parser.add_argument('--data_type', default='none', type=str, required=False,
                        choices=['p',
                                 'n',
                                'all',
                                'none'], 
                        help='(default=%(default)s)')
    parser.add_argument('--trainer', type=str, required=True, 
                        choices=['gan', 
                                 'gaussian', 
                                 'vae'])
    parser.add_argument('--mean_model_type', default='mlp', type=str, required=False,
                        choices=['mlp'], 
                        help='(default=%(default)s)')
    parser.add_argument('--gan_model_type', default='vae1', type=str, required=False,
                        choices=['vae1'], 
                        help='(default=%(default)s)')
    parser.add_argument('--seed', type=int, default=0,
                        help='Seeds4 values to be used; seed introduces randomness by changing order of classes')
    parser.add_argument('--mean_lr', type=float, default=5e-5,
                        help='learning rate (default: 5e-5. Note that mean_lr is decayed by args.gamma parameter args.schedule ')
    parser.add_argument('--vae_lr', type=float, default=0.0001,
                        help='learning rate (default: 0.0001. Note that g_lr is decayed by args.gamma parameter args.schedule ')
    parser.add_argument('--noise_d', default=100, type=int, required=False, help='(default=%(default)d)')
    parser.add_argument('--mean_hidden_dim', default=100, type=int, required=False, help='(default=%(default)d)')
    parser.add_argument('--vae_hidden_dim', default=100, type=int, required=False, help='(default=%(default)d)')
    parser.add_argument('--batch_size', type=int, default=32, metavar='N',
                        help='input batch size for training (default: 32)')
    parser.add_argument('--mean_nepochs', type=int, default=1000, help='Number of epochs for each mean increment')
    parser.add_argument('--vae_nepochs', type=int, default=200, help='Number of epochs for each gan increment')    
    parser.add_argument('--workers', type=int, default=0, help='Number of workers in Dataloaders')
    parser.add_argument('--num_of_input', type=int, default=4, help='Number of input for data')
    parser.add_argument('--num_of_output', type=int, default=6, help='Number of output for data')
    parser.add_argument('--sample_num', type=int, default=50, help='sampling number')

    
#     parser = deepspeed.add_config_arguments(parser)
    args=parser.parse_args()

    return args